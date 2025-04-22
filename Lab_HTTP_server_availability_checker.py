"""
Objectives

Learn how to:
use the socket module and its basic functionalities;
manage simple http connections.

Scenario
Write a simple CLI tool to diagnose the current status of a particular http server.
The tool should accept one or two command line arguments:
* (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be extremely simple,
we just want to know if the server is dead or alive)
* (optional) the server's port number (any absence of the argument means that the tool should use port 80)
use the HEAD method instead of GET — it forces the server to send the full response header but without any content;
it's enough to check if the server is working properly; the rest of the request remains the same as for GET.

We also assume that:
the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error message and returns an exit code equal to 1;
if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535, the tool prints an error message and returns an exit code equal to 2;
if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
if the connection succeeds, the very first line of the server’s response is printed.

Hints:
to access command line arguments, use the argv variable from the sys module;
its length is always one more than the actual number of arguments, as argv[0] stores your script's name;
this means that the first argument is at argv[1] and the second at argv[2]; don't forget that the command line arguments are always strings!
returning an exit code equal to n can be achieved by invoking the exit(n) function.

The tool is placed in a source file name sitechecker.py.

"""
import sys
import socket


def checker():
    if len(sys.argv) not in [2, 3]:
        print('Improper number of args: at least 1 is required and not more then 2 are allowed:\n'
              '- http server address required\n'
              '- port number (default is 80)')
        return exit(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        if len(sys.argv) == 2:
            sock.connect((sys.argv[1], 80))
        else:
            if int(sys.argv[2]) not in range(1, 65535):
                print('Port number is invalid - exiting')
                return exit(2)
            sock.connect((sys.argv[1], int(sys.argv[2])))
        sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
                  bytes(sys.argv[1], "utf8") +
                  b"\r\nConnection: close\r\n\r\n")
        print((sock.recv(1024).decode('utf-8')).splitlines()[0])
    except socket.timeout:
        print("Connection timed out!")
        return exit(3)
    except socket.error:
        print("Socket error")
        return exit(4)
    finally:
        sock.close()


if __name__ == "__main__":
    checker()


"""
> python checker.py www.google.com
HTTP/1.1 200 OK
"""
