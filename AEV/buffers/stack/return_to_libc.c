#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void secret(){
	printf("Secret message\n");
	exit(0);
}

char foo(size_t size, char* arg){
	char buffer[8];
	printf("buffer: %p\n", &buffer);
	
	memcpy(buffer, arg, size);

	return buffer[0];
}

int main(int argc, char* argv[]){
	char buffer[64];
	if(argc != 2)
		return -1;

	printf("secret: %p\n", &secret);
	printf("system: %p\n", &system);

	FILE *fp = fopen(argv[1], "r");
	size_t size = fread(buffer, 1, 64, fp);
	fclose(fp);
	
	foo(size, buffer);

	return 0;
}
