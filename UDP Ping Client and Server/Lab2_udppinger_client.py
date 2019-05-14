from datetime import datetime
from socket import *
from time import time

def main():

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = 'ping'

    total = 10
    i = 0

    while i < total:
        i++
        print ('\nping #: ', i)

        a = datetime.now()
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        clientSocket.settimeout(1)

        try:
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)

            b = datetime.now()
            c = a-b;
            print ('round trip time: ',c.microseconds, 'ms')
        except timeout:
            print ('ping timeout')

    clientSocket.close()

    pass

if __name__ == '__main__':
    main()
