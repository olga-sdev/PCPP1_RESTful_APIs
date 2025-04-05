"""
Socket module provides a class named socket which encapsulates a bundle of properties and activities related to the actual sockets' behaviour. 

The constants  and  are used when creating a socket object:
* AF_INET -> the address family for the socket / specify the Internet socket domain. It is used for IPv4 addresses. If you were using IPv6, you would use AF_INET6;
* SOCK_STREAM -> specifies the socket type. It is used for creating a TCP (Transmission Control Protocol) socket, which provides reliable, ordered, and error-checked data delivery between applications.
* connect() -> tries to connect your socket to the service of the specified address and port (service) number.

Conversation with the HTTP server consists of REQUESTS (sent by the client) and RESPONSES (sent by the server).

s.send -> method is used to send data over a socket (data in the form of a byte string).

send() may not send all the data in one go; for reliable data transfer, consider using sendall() instead.

recv() -> waits for the server's response, gets it, and puts it inside a newly created object of type bytes.
The argument in recv(arg) specifies the maximal acceptable length of the data to be received. 
If the server's response is longer than this limit, it will remain unreceived.

shutdown() -> method in Python is used to disable sending and/or receiving data on a socket.

Argument in shutdown(args):
* socket.SHUT_RD -> Stops receiving data.
* socket.SHUT_WR -> Stops sending data.
* socket.SHUT_RDWR -> Stops both sending and receiving.

close() -> closing a socket releases the resources associated with it, ensuring that it is properly cleaned up.
"""
import socket


server_addr = 'www.google.com'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_addr, 80))
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)
sock.shutdown(socket.SHUT_RDWR)
sock.close()
print(repr(reply))
