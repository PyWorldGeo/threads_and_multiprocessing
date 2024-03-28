import socket
import threading
import random

host = "127.0.0.1"
server_port = 55555
client_port = random.randint(8000, 9000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((host, client_port))
name = input("Nickname: ")

def receive():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass


thread1 = threading.Thread(target=receive)
thread1.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), (host, server_port))

while True:
    message = input("")
    if message == "quit":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), (host, server_port))
