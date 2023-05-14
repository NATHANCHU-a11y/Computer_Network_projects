import socket
import threading
import os

clients = []
client_ports = {}  # New dictionary to store client sockets and their ports
rec_folder = "rec"

if not os.path.exists(rec_folder):
    os.makedirs(rec_folder)


def save_file(client, filename):
    file_size = int(client.recv(1024).decode('utf-8'))
    received_size = 0
    save_path = os.path.join(rec_folder, filename)
    with open(save_path, 'wb') as file:
        while received_size < file_size:
            file_data = client.recv(1024)
            received_size += len(file_data)
            file.write(file_data)
    print(f"{filename} has been received and saved in the {rec_folder} folder.")


def forward_message(sender, message):
    for client in clients:
        if client != sender:
            client.send(message.encode('utf-8'))


def handle(client, port):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg.startswith("TRANSFER "):
                filename = msg.split(" ", 1)[1]
                save_file(client, filename)
                forward_message(client, f"Client {client.getpeername()} sent a file: {filename}")
            else:
                print(f"Message from {client.getpeername()} on port {port}: {msg}")
                forward_message(client, f"Client {client.getpeername()} on port {port}: {msg}")

                if msg == "exit":
                    break
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Client {client.getpeername()} on port {port} disconnected")
    clients.remove(client)
    del client_ports[client]
    client.close()


def receive(server, port):
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)} on port {port}")
        clients.append(client)
        client_ports[client] = port
        thread = threading.Thread(target=handle, args=(client, port))
        thread.start()


def main(port):
    host = '127.0.0.1'
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Server is listening on {host}:{port}")
    receive(server, port)

if __name__ == "__main__":
    ports = [5555, 5556, 5557]
    for port in ports:
        thread = threading.Thread(target=main, args=(port,))
        thread.start()