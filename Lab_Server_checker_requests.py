"""
Objectives
Learn how to:
use the requests module facilities;
interpret server responses.

Scenario
Return to the issues discussed in lab #1. Exactly the same functionality, but with the requests module instead of the socket module.
Everything else should remain the same: the command line arguments and outputs have to be indistinguishable.

Hint: use the head() method instead of get().
"""
import sys
import requests


def checker():
    if len(sys.argv) not in [2, 3]:
        print('Improper number of args: at least 1 is required and not more then 2 are allowed:\n'
              '- http server address required\n'
              '- port number (default is 80)')
        return exit(1)
    try:
        # Attempt to connect to a server
        if len(sys.argv) == 2:
            head_reply = requests.head(f'{sys.argv[1]}:{80}')
        else:
            if int(sys.argv[2]) not in range(1, 65535):
                print('Port number is invalid - exiting')
                return exit(2)
            head_reply = requests.head(f'{sys.argv[1]}:{int(sys.argv[2])}')
        print(head_reply)
    except requests.exceptions.Timeout:
        print('Timeout was exceeded. No data will be returned')
        return exit(3)
    except requests.exceptions.ConnectionError:
        print('Connection error has happened')
        return exit(4)


if __name__ == "__main__":
    checker()
