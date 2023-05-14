# Computer Network Project3
### Name1:Tianle Zhu   UFID:40105598
### Name2:Yan Gu       UFID:46562620

## 1. Description
This is a Python script for a chat client/server that uses sockets to communicate with each other. It allows clients to connect to the server and send messages to one another, as well as transfer files.

## 2. Instructions for Execution
Open three or more terminal windows on your computer and run following commands in the terminal.

### To Run Server
- ```cd desktop/CNproject1 ``` navigate to the directory of your project file
- ```python ftpserver.py``` to start the server

### To Run Client
- ```cd desktop/CNproject1 ``` navigate to the directory of your project file
- ```python ftpclient.py``` to start the client
- Enter a nickname when prompted
- Enter the port number to connect to

## 3. Working process of the Program
- The server starts first and listens on the certain port 5555/5556/5557.
- Once the server is running, clients can connect to it using the client.py script. The server will handle communication between multiple clients, allowing them to send and receive messages and files.
- When a client connects to the server, it is assigned a unique port number. This port number is stored in the client_ports dictionary, along with the client's socket. This allows the server to send messages to specific clients based on their port number.
- To send a message, simply type your message and press enter. Your message will be sent to the server and then broadcasted to all connected clients.
- To transfer a file, type "transfer " followed by the name of the file you wish to send.
- The file transfer will then be initiated and the file will be sent to the server, which will then broadcast it to the intended recipient(s).

### Notice
- The file could be arbitrarily large, so the file contents are splited into chunks of 1K bytes.
- The file data are writed into a new file in the "rec" folder, and prints a message indicating that the file has been received and saved.