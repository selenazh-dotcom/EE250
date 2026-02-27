"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> terminate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "192.168.0.159"
#HOST = "192.168.64.2"
PORT = 9090

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))

    # TODO: Get user input and send it to the server using your TCP socket
        print("Enter input: ")
        userinput = input()
        s.sendall(userinput.encode())
   
   # TODO: Receive a response from the server and close the TCP connection
        data = s.recv(1024)
        print(data)
        s.close()
    pass


if __name__ == '__main__':
    main()
