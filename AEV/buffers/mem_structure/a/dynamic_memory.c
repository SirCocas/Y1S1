#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(int argc, char* argv[]){
	char* buffer = (char*) malloc(10);
	char* str = buffer;

	free(buffer);
	
	// Write after free
	memcpy(str, "Hello World!!!!", 15); 
	// Read after free
	printf("%s\n", str);
}
