from socket import *
import sys

serverIP = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', int(sys.argv[1])))
clientSocket.sendto(sys.argv[2].encode(), (serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

clientSocket.close()
