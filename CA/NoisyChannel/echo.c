#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <assert.h>

#include "util.h"

int
main ( int argc, char * argv[] )
{
    uint16_t N;
    int16_t r_len;
    uint32_t len;
    uint8_t * m, * R;
    uint8_t ack;

    read( 5, &N, sizeof(N) );

    fprintf( stderr, "%s: N = %hu\n", argv[0], N );

    for (;;) {
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
        // fprintf( stderr, "r_len = %hu, len = %u\n", r_len, len );

        m = malloc( len );
        exact_read( 3, m, len ); // Read m

        write( 6, &ack, 1 ); // Ack reception

        if (ack == 1) {
            write( 4, m, len ); // Write m back
            write( 6, &ack, 1 ); // Signal end of message
        }

        free( R );
        free( m );
    }
}
