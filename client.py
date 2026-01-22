import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NAME':
                name = input("Enter your name: ")
                client.send(name.encode())
            else:
                print(message)
        except:
            break

def send():
    while True:
        msg = input()
        client.send(msg.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
