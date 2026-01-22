import socket
import threading

clients = {} 

def handle_client(conn, addr):
    try:
        name = conn.recv(1024).decode()
        clients[name] = conn
        print(f"{name} התחבר מ-{addr}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            dst_name, msg = data.split(":", 1)
            if dst_name in clients:
                clients[dst_name].send(f"{name}: {msg}".encode())
    finally:
        print(f"{name} התנתק")
        del clients[name]
        conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 12345))
    server.listen()
    print("Server is running on port 12345...")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
