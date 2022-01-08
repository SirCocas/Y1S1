#include <stdio.h>
#include <string.h>

void foo(int size, char* arg){
	char buffer[64];
	
	if(size > 0){
		memcpy(buffer, arg, size);
		buffer[size] = 0;
	}

	for(int i = 0; i<64; i++)
		printf("%c", buffer[i]);

	printf("\n");
}

int main(int argc, char* argv[]){
	char* secret = "Secret Message";
	int size = 0;
	
	sscanf(argv[1], "%d", &size);
	foo(size, argv[2]);

	return 0;
}
