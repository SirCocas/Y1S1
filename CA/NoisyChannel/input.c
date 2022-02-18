#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>

#include "util.h"

int
main ( int argc, char * argv[] )
{
    uint16_t N;
    int16_t r_len;
    uint32_t len, buffer_len, pad_len;
    uint8_t * m, * R, * buffer, * padding;
    uint8_t ack = 0;

    exact_read( 5, &N, sizeof(N) );

    fprintf( stderr, "%s: N = %hu\n", argv[0], N );

    buffer_len = ((1024 + N - 1) / N) * N;
    buffer = malloc( buffer_len );
    padding = malloc( N );

    for (;;) {
        // Read from stdin and send N-byte padded message

        len = read( 0, buffer, buffer_len - N );

        if (len < 1) exit( 0 );

        // Write original data
        
        write( 4, buffer, len );

        // Write padding
        
        pad_len = N - (len % N);
        memset( padding, (uint8_t) pad_len, pad_len );
        write( 4, padding, pad_len );

        // Write Ack to signal end of message

        write( 6, &ack, 1 );

        // Read noisy message until get it (possibly) correct
        
        for (ack = 0; ack != 1;) {
            exact_read( 5, &r_len, sizeof(r_len) ); // Read length of R

            if (r_len < 0) {
                // fprintf( stderr, "%s: redundancy block signaled bit flips\n", argv[0] );
                r_len = -r_len;
                ack = 0;
            }
            else {
                ack = 1;
            }

            R = malloc( r_len );
            exact_read( 5, R, r_len ); // Read R

            len = N * r_len;
            assert( len % N == 0 );

            m = malloc( len );
            exact_read( 3, m, len ); // Read m

            write( 6, &ack, 1 ); // Ack good reception

            // Assume that last byte provides accurate padding information

            if (ack == 1) {
                pad_len = m[len - 1];
                if (pad_len > N) { // Wrong value, assume no padding
                    pad_len = 0;
                }

                write( 1, m, len - pad_len );
            }

            free( R );
            free( m );
        }
    }
}
