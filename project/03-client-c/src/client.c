#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <stdlib.h>

int main (int argc, char *argv[]){

	int sock;
	struct sockaddr_in server;
	char msg[1000];
	char server_reply[2000];

	//create socket
	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock == -1){
		printf("Socket can't be created");
	}
	puts("Socket created");

	server.sin_addr.s_addr = inet_addr("172.18.0.3");
	server.sin_family = AF_INET;
	server.sin_port = htons (8998);

	//connect to remote server
	if (connect(sock, (struct sockaddr *)&server, sizeof(server))<0){
		puts("Connection failed");
		return 1;
	}
	puts("Connected");

	//server communication
	while (1){
		printf("Type your message: ");
		scanf("%s" , msg);

		//send data
		if (send(sock, msg, strlen(msg), 0) <0){
			puts("Data fail to send");
			return 1;
		}
		//reply from server
		if (recv(sock, server_reply, 2000, 0) <0){
			puts("Fail to receive");
			break;
		}
		puts ("Message from server: ");
		puts (server_reply);
	}
	close (sock);
	return 0;
}
