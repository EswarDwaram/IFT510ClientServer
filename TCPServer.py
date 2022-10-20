from socket import *

serverName = '10.153.0.206'
serverPort = 15000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print(f"The Server is listening on the port: {serverPort}")
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode())
    connectionSocket.close
