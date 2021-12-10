from socket import *

server_port = 33330

#initialize server socket
sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.bind(("localhost", server_port))
sSocket.listen(1)

#accepts connection from client
connection, addr = sSocket.accept()

#prints client's address and port
client_addr, client_port = addr
print("Connection from client with address", client_addr, "on port", client_port)
print("Type /q to quit chat")

while True: #wait until client sends message
    print("Waiting for message from client...")
    recv = connection.recv(1024).decode() #receive message from client
    if recv == "/q": #client quits chat
        break
    print("CLIENT:", recv)
    message = input(">>>")
    connection.send(message.encode()) #send message to client
    if message == "/q": #server quits chat
        break

#closes connection and socket
connection.close()
sSocket.close()