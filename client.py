import socket
import threading
import os
import time

nickname = input("Choose a nickname: ")

host = '127.0.0.1'
port = int(input("Enter the port number to connect: "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))


def send_file(filename):
    if os.path.exists(filename):
        client.send(f"TRANSFER {filename}".encode('utf-8'))
        file_size = os.path.getsize(filename)
        client.send(str(file_size).encode('utf-8'))

        with open(filename, 'rb') as file:
            file_data = file.read(1024)
            while file_data:
                client.send(file_data)
                file_data = file.read(1024)
                time.sleep(0.01)  # Add a small delay between sending file chunks
        print(f"{filename} has been sent.")
    else:
        print(f"{filename} does not exist.")


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break


def write():
    while True:
        message = input('')
        if message.startswith("transfer "):
            filename = message.split(" ", 1)[1]
            send_file(filename)
        else:
            msg_to_send = f"{nickname}: {message}"
            client.send(msg_to_send.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
