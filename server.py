import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

clients = {}

def handle_client(client_socket, client_name):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            target, msg = message.split(":", 1)
            target = target.strip()

            if target in clients:
                clients[target].send(f"{client_name}: {msg}".encode())
            else:
                client_socket.send("User not found".encode())
    except:
        pass
    finally:
        print(f"{client_name} disconnected")
        del clients[client_name]
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server is running...")

    while True:
        client_socket, addr = server.accept()
        client_socket.send("NAME".encode())
        name = client_socket.recv(1024).decode()

        clients[name] = client_socket
        print(f"{name} connected")

        thread = threading.Thread(target=handle_client, args=(client_socket, name))
        thread.start()

start_server()
