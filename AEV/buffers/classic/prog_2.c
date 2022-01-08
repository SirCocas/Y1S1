#include <stdio.h>
#include <string.h>

int main() {
	char allowed = 0;
	char password[8];
	char username[8];
	char message[32];

	puts("username:");
	gets(username);
	puts("password:");
	gets(password);
	allowed = strcmp("admin", username) + strcmp("topsecrt", password);
	
	puts("message:");
	gets(message);

	printf("user=%s pass=%s result=%d\n", username, password, allowed);

	if(allowed == 0)
		printf("Access granted. Message sent!\n");
	else
		printf("Access denied\n");

	return 0;
}

