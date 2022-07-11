from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print("This message: ",modifiedMessage)
    print("is received from: ", clientAddress)
    ToUpperMsg = modifiedMessage.upper()
    serverSocket.sendto(ToUpperMsg.encode(), clientAddress)
