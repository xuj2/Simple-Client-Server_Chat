from socket import *

server_name = "localhost"
server_port = 33330

#initialize client socket
cSocket = socket(AF_INET, SOCK_STREAM)
cSocket.connect((server_name, server_port))

#prints server's address and port
print("Connected to server with address", gethostbyname(server_name), "on port", server_port)
print("Type /q to quit chat")

while True:
    message = input(">>>")
    cSocket.send(message.encode()) #send message to server
    if message == "/q": #client quits chat
        break
    while True: #wait until server sends message
        print("Waiting for message from server...")
        recv = cSocket.recv(1024).decode() #receive message from server
        if recv == "/q": #server quits chat
            cSocket.close() #closes socket and exit program
            exit()
        print("SERVER:", recv)
        break

#closes socket
cSocket.close()