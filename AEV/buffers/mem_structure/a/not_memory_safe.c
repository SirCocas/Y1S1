#include <stdio.h>

void main(int argc, char* argv[]){
	int buffer = 4;
	int *value = &buffer;

	// Correct usage
	printf("%d\n", *value);

	// Reading memory after the variable
	printf("%d\n", *(value + 4));
	
	// Reading memory before the variable
	printf("%d\n", *(value - 4));

}
