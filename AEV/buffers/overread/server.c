#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> 
#include <string.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <arpa/inet.h> 
#include <netinet/in.h> 
  
#define PORT    8080 
 
#define MESSAGE_SIZE 128

int main() { 
    char buffer[32];
    int n;
    int sockfd; 
    struct sockaddr_in servaddr, cliaddr; 
    int len = sizeof(cliaddr);
      
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
      
    memset(aux, 0, sizeof(int));
    memset(&servaddr, 0, sizeof(servaddr)); 
    memset(&cliaddr, 0, sizeof(cliaddr)); 
      
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = INADDR_ANY; 
    servaddr.sin_port = htons(PORT); 
      
    bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr));
    while(1){
	    n = recvfrom(sockfd, buffer, 32, NULL, &cliaddr, &len); 
	    printf("%s\n", buffer);
	    sendto(sockfd, buffer, MESSAGE_SIZE, NULL, &cliaddr, len); 
    }
    printf("Exit\n");
    return 0; 
} 
