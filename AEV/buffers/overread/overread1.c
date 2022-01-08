#include <string.h>
#include <stdio.h>


int main(int argc, char* argv[]){
	char message[32];
	char buffer[8];
	
	printf("Password: ");
	gets(buffer);
	
	sprintf(message, "Secret message");

	if(strcmp(buffer, "password") == 0) {
		printf("%s\n", message);
	}else{
		printf("Password %s is incorrect\n", buffer);
	}
}
