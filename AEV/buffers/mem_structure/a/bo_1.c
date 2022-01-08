#include <stdio.h>

void main(int argc, char* argv[]){
	char message[] = "Hello World";
	char buffer[5];
	int i;

	printf("%s\n", message);
	for(i = 0;i < 15; i++) { 
		buffer[i] = 'A';
	}
	printf("%s %s\n", buffer, message);
}
