import socket
import threading


# Choosing Nickname
nickname = input("Choose your nickname: ")


host = "127.0.0.1"  # The server's hostname or IP address


port = 55555  # The port used by the server

#It creates a socket object, uses .connect() to connect to the server, it calls s.recv() to read the server’s reply and then prints it.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The client calls .connect() to establish a connection to the server
client.connect((host, port))

#data is exchanged between the client and server using calls to .send() and .recv()
# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()