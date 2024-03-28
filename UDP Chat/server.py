import socket
import threading
import queue

messages = queue.Queue()
clients = []

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((host, port))
#UDP is a connectionless, unreliable datagram, (message) protocol, so no need to listen for new connections
# datagrams can come in in any order from any source."

def receive():
    print("Server Started!")
    while True:
        try:
            #The recvfrom() system call receives a message from a socket and capture the address from which the data was sent. Unlike the recv() call, which can only be used on a connected stream socket or bound datagram socket,
            # recvfrom() can be used to receive data on a socket whether or not it is connected.
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))

        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
            #Remove and return an item from the queue
            message, addr = messages.get()
            print(message.decode())
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().split(":")[0] == "SIGNUP_TAG":
                        name = message.decode()[11:]
                        server.sendto(f"{name} joined!".encode(), client)
                    else:
                        #send() is used for TCP SOCK_STREAM connected sockets, and sendto() is used for UDP SOCK_DGRAM unconnected datagram sockets.
                        server.sendto(message, client)
                except:
                    clients.remove(client)

thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=broadcast)

thread1.start()
thread2.start()