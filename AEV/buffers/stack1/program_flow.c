#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void secret(){
	printf("Secret message\n");
	exit(0);
}

char foo(int size, char* arg){
	char buffer[8];
	
	memcpy(buffer, arg, size);

	return buffer[0];
}

int main(int argc, char* argv[]){
	char buffer[64];
	if(argc != 2)
		return -1;

	printf("%p\n", &secret);

	FILE *fp = fopen(argv[1], "r");
	int size = fread(buffer, 1, 64, fp);
	fclose(fp);
		
	foo(size, buffer);

	return 0;
}
