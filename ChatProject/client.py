import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))

    name = input("Enter your name: ")
    client.send(name.encode())

    def receive():
        while True:
            try:
                print(client.recv(1024).decode())
            except:
                break

    import threading
    threading.Thread(target=receive, daemon=True).start()

    while True:
        try:
            dst = input("Send to (client name): ")
            msg = input("Message: ")
            client.send(f"{dst}:{msg}".encode())
        except:
            break

if __name__ == "__main__":
    main()
