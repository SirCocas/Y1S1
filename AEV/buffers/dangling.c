#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <malloc.h>

#define BUFSIZE 16

int main(int argc, char **argv) {
	char *buf1 = (char *) malloc(BUFSIZE*100);
	memset(buf1, 'U', BUFSIZE);
	free(buf1);

	char *buf2 = (char *) malloc(BUFSIZE);
	memset(buf2, 'A', BUFSIZE);
	
	printf("%s\n", buf1);
}
