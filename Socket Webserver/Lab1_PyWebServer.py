#import socket module
from socket import *
serverPort=80
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end

    try:
        #Fill in start    #Fill in end
        message = connectionSocket.recv(1024)
        if message != '':
            try: 
                filename = str(message).split()[1]
                print('Serving ', filename)
                f = open(filename[1:]) 
                outputdata = f.read() #Fill in
                print(outputdata);
                #Send one HTTP header line into socket
                #Fill in start
                #connectionSocket.send("HTTP/1.1 200 OK\n".encode())
                #Fill in end
                #Send the content of the requested file to the client
                connectionSocket.send(outputdata.encode())
                connectionSocket.close()
            except IndexError:
                connectionSocket.send("HTTP/1.1 500 Server Error\n".encode())
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\n".encode())
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 
