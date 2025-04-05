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

"""
b'HTTP/1.1 200 OK\r\nDate: Sat, 05 Apr 2025 12:05:04 GMT\r\nExpires: -1
\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1
\r\nContent-Security-Policy-Report-Only: object-src \'none\';base-uri \'self\';script-src \'nonce-0Q_0QGaG8ROk2njTLVY9zA\' \'strict-dynamic\' \'report-sample\' \'unsafe-eval\' \'unsafe-inline\' 
https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp\r\nServer: gws\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN
\r\nSet-Cookie: AEC=AVcja2cMaSIsRL8obFtoxyYIupkKMBLKKDx0OA_QbtaiLpmw-lTVBIiXqw; expires=Thu, 02-Oct-2025 12:05:04 GMT; path=/; domain=.google.com; Secure; HttpOnly; 
SameSite=lax\r\nAccept-Ranges: none\r\nVary: 
Accept-Encoding\r\nConnection: close\r\nTransfer-Encoding: chunked\r\n\r\n4f40\r\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="nl"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="0Q_0QGaG8ROk2njTLVY9zA">(function(){var _g={kEI:\'cBzxZ8SzMozt7_UPtZq3oAU\',
kEXPI:\'0,202792,25,4037228,78813,16105,344796,94243,195801,5241682,57,14,36,36812535,25228681,42877,95391,8182,10491,4381,56223,6757,23879,9140,4598,328,6226,34311,16264,3615,24,9242,709,1341,5329,6463,1915,50,15585,58708,21345,8341,41,13162,477,1,4922,617,1202,4105,7737,3347,7739,2285,4945,2147,2833,1784,5774,4'
"""
