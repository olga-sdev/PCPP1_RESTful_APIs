_Socket (end-point)_ -> point where the DATA is available to get it FROM and where the data may be sent TO.

POSIX (a standard of contemporary Unix-class operating systems).

BSD sockets - the name was borrowed from Berkeley Software Distribution, the name of a Unix-class operating system, where the sockets were deployed for the very first time.

Socket domains main:
* UNIX -> Used for local communication between processes on the same host. It uses file paths as addresses.
* INET -> Supports communication between hosts over a network (IPv4-based, IPv6-based).
* NETLINK -> Used for communication between the kernel and user-space processes.
* BLUETOOTH -> Designed for Bluetooth communication.
* PACKET -> Provides low-level access to network packets.

Socket address.
INET domain sockets are identified (addressed) by pairs of values:
* IP address of the computer system inside which the socked is located;
* port number (more often referred to as service number)

IP4 address -> 32-bit long value used to identify computers connected to any TCP/IP network: 4 numbers from the range 0..255

IP6 address -> 128 bits.

socket/service number is a 16-bit long integer number identifying a socket within a particular system

Well-Known Ports (0–1023): Reserved for widely-used protocols
* HTTP protocol -> port 80
* HTTPS -> 443
* FTP -> 21

Registered Ports (1024–49151): Assigned by IANA for specific services or applications.

Dynamic/Private Ports (49152–65535): Used dynamically by applications for temporary communication.

A protocol is a standardized set of rules allowing processes to communicate with each other.
