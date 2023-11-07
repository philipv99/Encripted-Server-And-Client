from socket import *
import threading
import ssl

certificatesDirectory = 'C:/certificates'
privatePath = certificatesDirectory + 'key.pem'
certificatesPath = certificatesDirectory + 'certificate.pem'
privatekeyPassword = "philip"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(cerfile = certificatesPath, keyfile=privatePath, password=privatekeyPassword)


def handle_client(connection_socket, address):
   print(address)
   sentence = connection_socket.recv(1024).decode()
   print(sentence)
   capitalized_sentence = sentence.upper()
   connection_socket.send(capitalized_sentence.encode())
   connection_socket.cloce()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("server is ready to listen")

while True:
   connectionSocket, addr = serverSocket.accept()
   threading.Thread(target=handle_client, args=(connectionSocket, addr)).start() 