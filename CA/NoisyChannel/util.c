#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

#include "util.h"

void
exact_read( int fd, void * to, int len )
{
    uint8_t * _to = to;
    int ret;
    
    while (len) {
        ret = read( fd, _to, len );

        if (ret == 0) {
            // fprintf( stderr, "Read source closed\n" );
            exit( 0 );
        }
        else if (ret == -1) {
            // fprintf( stderr, "Error while reading from source\n" );
            exit( 0 );
        }

        _to += ret;
        len -= ret;
    }
}
