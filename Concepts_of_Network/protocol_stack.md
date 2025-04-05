_Protocol stack_ -> collection of protocols that work together to enable network communication. 

It's multilayer, where each layer handles a specific aspect of data transmission. 

The most well-known protocol stack is the *TCP/IP model*, which is the foundation of the internet.

![image](https://github.com/user-attachments/assets/d000d03d-955e-4add-9cb5-5a619a0d1a14)

The TCP/IP stack consists of four layers:

* _Application Layer_ -> software apps interact with the network (e.g., HTTP, FTP);
* _Transport Layer_ -> responsible for reliable data transfer (e.g., TCP, UDP);
* _Internet Layer_ -> handles routing and addressing (e.g., IP);
* _Network Interface Layer_ manages hardware-level data transmission.

Elementary services are located at the bottom of the stack, while the most advanced and abstractive lie on the top.

*IP (Internetwork Protocol)* is one of the lowest parts of TCP/IP protocol stack. 
Functionality: send a packet of data between two network nodes.

It doesn't guarantee that:
* data will _reach the target_ (moreover, if any of the datagrams is lost, it may remain undetected);
* data will reach the target _intact_;
* data will reach the target _in the same order_ as they were sent;

The upper layers are able to compensate all these IP's infirmities.

_TCP (Transmission Control Protocol)_ is the highest part of the TCP/IP protocol stack. 
It uses data (provided by the lower layers) and handshakes (an automated process of synchronizing the flow of data) to construct a reliable communication channel able to transmit and receive single characters.

It guarantees that:

* stream of _data reaches the target_, or the sender is informed that communication has failed;
* data reaches the target _intact_.

_UDP (User Datagram Protocol)_ lies at the higher part of TCP/IP protocol stack, but lower than the TCP. 

It doesn't use handshakes-> and:
* faster than TCP (due to fewer overheads)
* less reliable than TCP.

TCP is a first-choice protocol for applications where _data safety_ is more important that efficiency (e.g., WWW, REST, mail transfer, etc.).

UDP is more adequate for applications where _response time_ is crucial (DNS, DHCP, etc.)
