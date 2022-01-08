#include <stdio.h>

void main(int argc, char* argv[]){
	int value = 42;

	// Correct usage
	printf("%d\n", value);

	// Cast to variable with different storage
	printf("%f\n", *((double*) &value));
	
	// Cast to variable with different size
	printf("%llu\n", *((unsigned long long*) &value));
	
	printf("%s\n", ((char*) &value));

}
