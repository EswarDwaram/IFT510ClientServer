from socket import *

serverName = 'DESKTOP-PBERADQ'
serverPort = 15000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
message = input('Enter your message')

clientSocket.send(message.encode())
modifiedMessage = clientSocket.recvfrom(2048)
print("Message from Server:", f"..... {modifiedMessage.decode()}")
clientSocket.close()