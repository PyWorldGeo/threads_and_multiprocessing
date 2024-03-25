import socket
import threading

#host can be a hostname, IP address, or empty string. If an IP address is used, host should be an IPv4-formatted address string.
host = "127.0.0.1"  # Standard loopback interface address (localhost)

#port represents the TCP port number to accept connections on from clients. It should be an integer from 1 to 65535, as 0 is reserved.
# Some systems may require superuser privileges if the port number is less than 1024.
port = 55555  # Port to listen on (non-privileged ports are > 1023)

# Starting Server
# You’re going to create a socket object using socket.socket(), specifying the socket type as socket.SOCK_STREAM.
# When you do that, the default protocol that’s used is the Transmission Control Protocol (TCP).

#1 #The arguments passed to socket() are constants used to specify the address family and socket type. AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2 The .bind() method is used to associate the socket with a specific network interface and port number.
#The values passed to .bind() depend on the address family of the socket. In this example, you’re using socket.AF_INET (IPv4).
# So it expects a two-tuple: (host, port).
server.bind((host, port))

#3 A listening socket does just what its name suggests. It listens for connections from clients.
#.listen() enables a server to accept connections.
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients. The server will simply echo whatever it receives back to the client
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

#data is exchanged between the client and server using calls to .send() and .recv()
# Receiving / Listening Function
def receive():
    while True:
        #4 When a client connects, the server calls .accept() to accept, or complete, the connection.
        #The .accept() method blocks execution and waits for an incoming connection. When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.
        # The tuple will contain (host, port) for IPv4 connections or (host, port, flowinfo, scopeid) for IPv6.
        client, address = server.accept()
        #you now have a new socket object from .accept(). It’s the socket that you’ll use to communicate with the client.
        # It’s distinct from the listening socket that the server is using to accept new connections:
        #After.accept() provides the client socket object client, an infinite while loop is used to loop over blocking calls to conn.recv().
        # This reads whatever data the client sends

        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()