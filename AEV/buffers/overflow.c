#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define BUFSIZE 8

int main(int argc, char **argv) {
	char *buf1 = (char *) malloc(BUFSIZE);
	char *buf2 = (char *) malloc(BUFSIZE);
	memset(buf1, 0, BUFSIZE);
	memset(buf2, 0, BUFSIZE);

	printf("Buf2: %s\n", buf2);
	strcpy(buf1, argv[1]);
	printf("Buf2: %s\n", buf2);
}
