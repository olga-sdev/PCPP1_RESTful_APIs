"""
socket module provides a class named socket which encapsulates a bundle of properties and activities related to the actual sockets' behaviour. 

The constants  and  are used when creating a socket object:
* AF_INET -> the address family for the socket / specify the Internet socket domain. It is used for IPv4 addresses. If you were using IPv6, you would use AF_INET6;
* SOCK_STREAM -> specifies the socket type. It is used for creating a TCP (Transmission Control Protocol) socket, which provides reliable, ordered, and error-checked data delivery between applications.
"""
import socket

server_addr = input("Input server you want to connect to: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
