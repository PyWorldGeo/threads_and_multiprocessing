import socket
import threading

nickname = input("Enter Your Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 55555

client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "nick":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    while True:
        new_message = input('')
        message = f"{nickname}: {new_message}"
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()



