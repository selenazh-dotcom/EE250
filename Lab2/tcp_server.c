/* A simple server in the internet domain using TCP
 * Answer the questions below in your writeup
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    /* 1. What is argc and *argv[]?
     *   arcg is the amount of arguments being passed into main by the commamd line (integar value), while argv is the array that holds all of these arguments.
     */
    int sockfd, newsockfd, portno;
    /* 2. What is a UNIX file descriptor and file descriptor table?
     *	   A UNIX file descriptor is an identifier for the file, typically being representented as integars. The file descriptors are held in a file descriptor table, which is maintained by the kernel.
     */
    socklen_t clilen;

    struct sockaddr_in serv_addr, cli_addr;
    /* 3. What is a struct? What is the structure of sockaddr_in?
     *    A struct is a data type in which you can define and assign  different properties.
     *    
     *    According to online documentation, sockaddr_in has 3 properties: sa_family_t,
     *    in_port_t (port number), and another struct in_addr (IPv4 address)/
     */
    
    int n;
    if (argc < 2) {
        fprintf(stderr,"ERROR, no port provided\n");
        exit(1);
    }
    
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    /* 4. What are the input parameters and return value of socket()
     * 	    The input parameters include AF_INET, which specifies the domain of IPv4, SOCK_STREAM, 
     * 	    which indicates a socket with reliable 2-way connection-based byte stream. The last 
     * 	    input specifies the protocol. Usually if there's just a single protocol in the protocol 
     * 	    family for the socket, it's just 0.
     *
     * 	    Outputs include a file descriptor for the new socket. If there's an error, it will return
     * 	    a -1.
     *
     * 	    (according to Linux manual)
     */
    
    if (sockfd < 0) 
       error("ERROR opening socket");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    
    if (bind(sockfd, (struct sockaddr *) &serv_addr,
             sizeof(serv_addr)) < 0) 
             error("ERROR on binding");
    /* 5. What are the input parameters of bind() and listen()?
     *	    The input parameters of bind() are int sockfd (file descriptor), struct sockaddr (specifies the address),
     *	    and socklen_t structure address_len (byte size of address structure).
   	     
            THe input parameteres of listen() are int sockfd (file descriptor) and int backlog (max queue length).

	   (according to Linux manual) 
    */
    
    listen(sockfd,5);
    clilen = sizeof(cli_addr);
    
    while(1) {
        /* 6.  Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
        *    It uses a while(1) so that the code is stuck in this loop and continuously searches for possible connections to accept. 
	*    There might be problems if multiple simultaneous connections are happening because this code closes the socket after receiving a message from 1 connection. That means subsequent attempts at connecting will be unsuccessful.	
	*/

	char buffer[256];
        newsockfd = accept(sockfd, 
                    (struct sockaddr *) &cli_addr, 
                    &clilen);
	/* 7. Research how the command fork() works. How can it be applied here to better handle multiple connections?
         *    The command fork() creates child processes that can run in parallel with the main process. For example, if you used fork() n times while printing "Hello World", you would see that message get printed 2^n times. This is useful to handle multiple processes because you can open up multiple of the loops that stay open even if one of the sockets close. In that case, the maximum number of connections is also defined by 2^n, with n being the amount of fork()s.     
        */
        
	if (newsockfd < 0) 
             error("ERROR on accept");
	bzero(buffer,256);
        
	n = read(newsockfd,buffer,255);
        if (n < 0) 
            error("ERROR reading from socket");
        printf("Here is the message: %s\n",buffer);
        n = write(newsockfd,"I got your message",18);
        if (n < 0) 
            error("ERROR writing to socket");
        close(newsockfd);
    }
    close(sockfd);
    return 0; 
}
  
/* This program makes several system calls such as bind, and listen. What exactly is a system call?
 *	A system call is a way for the user to access an interface that allows them to request services from the kernel in a controlled manner. We can't access things in the kernel directly because the system would be too insecure. For example, we can pass file descriptors through system calls to allow the kernel to access the file and perform the process; the process would not have direct cnotact with the files.
 */

