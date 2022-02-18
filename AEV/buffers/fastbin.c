#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int main()
{
	//Fill up tcache first.
	void *ptrs[8];
	for (int i=0; i<8; i++) {
		ptrs[i] = malloc(8);
	}
	for (int i=0; i<7; i++) {
		free(ptrs[i]);
	}

	// Allocating 3 buffers
	int *a = calloc(1, 8);
	int *b = calloc(1, 8);
	int *c = calloc(1, 8);

	printf("1st calloc(1, 8): %p\n", a);
	printf("2nd calloc(1, 8): %p\n", b);
	printf("3rd calloc(1, 8): %p\n", c);

	free(a);
	free(b);
	free(a); //AGAIN!

	//Free list now has: a b a
	
	int *d = calloc(1, 8);
	int *e = calloc(1, 8);
	int *f = calloc(1, 8);

	printf("New buffers\n");
	printf("1rd calloc(1, 8): %p\n", d);
	printf("2rd calloc(1, 8): %p\n", e);
	printf("3rd calloc(1, 8): %p\n", f);
}
