#include <stdio.h>

char foo(int a){
	char local_a = 3;
	char buffer[16];
	int local_b = 5;
	printf("\nfoo\n");
	printf("a      : %p\n", &a);	
	printf("local_a: %p\n", &local_a);
	printf("buffer : %p\n", &buffer);
	printf("local_b: %p\n", &local_b);

	buffer[0] = local_a;
	return buffer[0];
}

int main(int argc, char* argv[]){
	printf("main\n");
	printf("argc   : %p\n", &argc);
	printf("argv   : %p\n", argv);

	return foo(argc);
}


