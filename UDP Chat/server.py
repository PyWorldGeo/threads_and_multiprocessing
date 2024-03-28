import socket
import threading
import queue

messages = queue.Queue()
clients = []

host = "127.0.0.1"
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((host, port))

def receive():
    print("Server Started!")
    while True:
        try:
            message, addr = server.recvfrom(1024)
            messages.put((message, addr))

        except:
            pass

def broadcast():
    while True:
        while not messages.empty():
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
                        server.sendto(message, client)
                except:
                    clients.remove(client)

thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=broadcast)

thread1.start()
thread2.start()