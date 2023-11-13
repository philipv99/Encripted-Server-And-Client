from socket import *
import ssl
import pprint

serverName = 'localhost'
serverPort = 12000
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
clientSocket = socket(AF_INET, SOCK_STREAM)
secureSocket = socket.wrap_socket(clientSocket)
clientSocket.connect((serverName, serverPort))
sentence = input('input sentence')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
clientSocket.close() 