#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/select.h>

#include "util.h"

#define MAX(x,y) ((x) > (y) ? (x) : (y))

uint16_t N;
double P;
char ** app1, ** app2;

int
dup_and_close( int from, int to )
{
    dup2( from, to );
    close( from );

    return to;
}

void
memxor( uint8_t * from, uint8_t * to, uint32_t len )
{
    while (len--) {
        *to++ ^= *from++;
    }
}

int
random_lower_than( int max )
{
    return rand() % max;
}

int
noise()
{
    return rand() < (int) (P * RAND_MAX);
}

void
add_noise( uint8_t * block, int len )
{
    int count = random_lower_than( len );

    // fprintf( stderr, "About to change %d bytes\n", count );

    for (int i = count; i > 0; i--) {
        int index = random_lower_than( len );
        int shift = random_lower_than( 8 );
        // fprintf( stderr, "Change bytes at offset %d by XORing it with 1 << %d\n", index, shift );
        block[index] ^= 1 << shift;
    }
}

void
calculate_R( uint8_t * m, uint32_t b_len, uint8_t * R )
{
    memset( R, 0, b_len );
    for (int i = 0; i < N; i++) { // for every block in m
        memxor( m + i * b_len, R, b_len );
    }
}

void
forward_noisy_message( int peer, int r_int, int e_int, int a_int )
{
    uint32_t len, b_len;
    uint8_t * m, * backup_m, * R, * new_R;
    int16_t r_len;
    uint8_t ack;

    exact_read( peer, &len, sizeof(len) );
    // fprintf ( stderr, "channel message len = %d\n", len );
    assert( len % N == 0 );
    b_len = len / N;

    backup_m = alloca( len );
    m = alloca( len );
    R = alloca( b_len );
    new_R = alloca( b_len );

    exact_read( peer, backup_m, len );

    for (;;) {
        memcpy( m, backup_m, len );
        
        // Create redundancy block

        calculate_R( m, b_len, R );

        r_len = b_len;

        // Add random noise
            
        if (P != 0) {
            for (int i = 0; i < N; i++) {
                if (noise()) {
                    // fprintf( stderr, "Added noise to block\n" );
                    add_noise( m + i * b_len, b_len );
                }
            }

            if (noise()) {
                // fprintf( stderr, "Added noise to R\n" );
                add_noise( R, b_len );
            }

            // Recalculate R to see if reveals errors
                
            calculate_R( m, b_len, new_R );
                
            if (memcmp( R, new_R, b_len) != 0) { // Errors detected
                r_len = -b_len;
            }
        }

        write( e_int, &r_len, sizeof(r_len) );
        write( e_int, R, b_len );
        write( r_int, m, len );

        exact_read( a_int, &ack, 1 );

        if (ack) return;
    }
}

void
forward_message( int peer, int w_int, int a_int )
{
    uint8_t * m;
    uint32_t len = 0;
    uint8_t buffer[1024];
    int buffer_len;
    int error;
    fd_set r_set;
    int nfds = MAX(w_int,a_int) + 1;

    for (;;) {
        FD_ZERO( &r_set );
        FD_SET( w_int, &r_set );
        FD_SET( a_int, &r_set );

        error = select( nfds, &r_set, 0, 0, 0 );

        if (error < 1 ) {
            exit( 0 );
        }
    
        if (FD_ISSET( w_int, &r_set )) { // Message chunk
            // fprintf( stderr, "Message chunk\n" );
            buffer_len = read( w_int, buffer, sizeof(buffer) );
            if (buffer_len < 1) {
                exit( 0 );
            }

            if (len == 0) {
                m = malloc( buffer_len );
            }
            else {
                m = realloc( m, len + buffer_len );
            }

            memcpy( m + len, buffer, buffer_len );
            len += buffer_len;

            continue; // Keep reading message chunks while present
        }

        if (FD_ISSET( a_int, &r_set )) { // Message is done
            // fprintf( stderr, "Message done\n" );
            exact_read( a_int, buffer, 1 );
            break;
        }
    }

   // Write message to the noisy channel, preceeded by its size (unsigned 32 bit integer)

    // fprintf ( stderr, "len = %d\n", len );
    write( peer, &len, sizeof(len) );
    write( peer, m, len );

    free( m );
}

void
noisy_channel( char * app, int r_peer, int w_peer, int r_int, int w_int, int e_int, int a_int )
{
    int nfds = MAX(r_peer,w_int) + 1;

    srand( getpid() );

    // Send N to App

    write( e_int, &N, sizeof(N) );

    // Loop forever listening for two reading endpoints 
    
    for(;;) {
        fd_set r_set;
        int error;

        FD_ZERO( &r_set );
        FD_SET( r_peer, &r_set );
        FD_SET( w_int, &r_set );

        if ((error = select( nfds, &r_set, 0, 0, 0 )) > 0) {
            if (FD_ISSET( r_peer, &r_set )) {
                // fprintf ( stderr, "channel -> %s\n", app );
                forward_noisy_message( r_peer, r_int, e_int, a_int );
            }

            if (FD_ISSET( w_int, &r_set )) {
                // fprintf ( stderr, "%s -> channel\n", app );
                forward_message( w_peer, w_int, a_int );
            }
        }

        if (error == -1) {
            exit( 0 );
        }
    }
}

void
app( char ** argv, int r_ch, int w_ch )
{
     pid_t pid = getpid();
     int r_int[2]; // Read interface
     int w_int[2]; // Write interface
     int e_int[2]; // Redundancy interface
     int a_int[2]; // Ack interface

     pipe( r_int );
     pipe( w_int );
     pipe( e_int );
     pipe( a_int );

     if (fork() == 0) { // App
         close( r_ch );
         close( w_ch );
         close( r_int[1] );
         close( w_int[0] );
         close( e_int[1] );
         close( a_int[0] );

         // Relocate descriptors to guaranty that 3 to 6 are free
         // Up to now, we never used 14 and above

         r_int[0] = dup_and_close( r_int[0], 14 );
         w_int[1] = dup_and_close( w_int[1], 15 );
         e_int[0] = dup_and_close( e_int[0], 16 );
         a_int[1] = dup_and_close( a_int[1], 17 );

         dup_and_close( r_int[0], 3 );
         dup_and_close( w_int[1], 4 );
         dup_and_close( e_int[0], 5 );
         dup_and_close( a_int[1], 6 );

         // fprintf ( stderr, "About to execute %s\n", argv[0] );
         execv( argv[0], argv );
     }
     else { // Noisy channel
         close( r_int[0] );
         close( w_int[1] );
         close( e_int[0] );
         close( a_int[1] );

         noisy_channel( argv[0], r_ch, w_ch, r_int[1], w_int[0], e_int[1], a_int[0] );
     }
}

int
main( int argc, char * argv[] )
{
    int LR[2];
    int RL[2];

    if (argc < 6) {
        fprintf ( stderr, "usage: %s N-value P-value app1 [app1_args] \\| app2 [app2_args]\n", argv[0] );
        exit( 2 );
    }

    if (sscanf( argv[1], "%hu", &N ) != 1 || argv[1][0] == '-' || N <= 1) {
        fprintf ( stderr, "Illegal N-value (%s), must be an integer greater than 1\n", argv[1] );
        exit( 2 );
    }

    if (sscanf( argv[2], "%lg", &P ) != 1 || P < 0 || P > 1) {
        fprintf ( stderr, "Illegal P-value (%s), must be a real in the interval [0, 1]\n", argv[2] );
        exit( 2 );
    }

    app1 = argv + 3;

    for (int i = 4; i < argc; i++) {
        if (strcmp( argv[i], "|" ) == 0) {
            app2 = argv + i + 1;
            argv[i] = 0; // Set the pointer to null to use app1 in exec
            goto go;
        }
    }

    fprintf ( stderr, "Found no separator of applications (|)\n" );
    exit( 2 );

go:

    // fprintf ( stderr, "We have a go!\n" );

    pipe( LR );
    pipe( RL );

    if (fork() == 0) { // Right channel
        close( LR[0] );
        close( RL[1] );
        // fprintf ( stderr, "App1: %s\n", app1[0] );
        app( app1, RL[0], LR[1] ); 
    }
    else { // Left channel
        close( RL[0] );
        close( LR[1] );
        // fprintf ( stderr, "App2: %s\n", app2[0] );
        app( app2, LR[0], RL[1] ); 
    }
}
