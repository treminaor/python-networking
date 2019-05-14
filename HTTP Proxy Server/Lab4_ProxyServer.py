from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Fill in start.
port = 8888
max_connections = 1
tcpSerSock.bind(('',port))
tcpSerSock.listen(max_connections)
# Fill in end.

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    print(message)
    # Extract the filename from the given message
    file = str( message, encoding='utf8' )
    print(file)
    filename = file.split()[1].split("/")[1]
    print (filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "rb")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send(b"HTTP/1.0 200 OK\r\n")
        tcpCliSock.send(b"Content-Type:text/html\r\n")
        # Fill in start.
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
        f.close()
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace('www.','',1)
            print('hostname: ', hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                try:
                    c.connect((hostn, 80))
                except socket.error as e:
                    print('socket error: ', e);
                print('socket connection success')
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('rwb')
                head = "GET " + "http://" + filename + " HTTP/1.0\n\n"
                headb = bytes(head,'utf-8')
                c.send(headb)
                fileobj.write(headb)
                # Read the response into buffer
                # Fill in start.
                buff = fileobj.readlines() # read all the files to the buffer

                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open('./' + filename,'wb')
                # Fill in start.
                for i in range(0, len(buff)):
                    tmpFile.write(buff[i])
                    tcpCliSock.send(buff[i])
                # Fill in end.
                tmpFile.close()
            except Exception as e:
                print(str(e))
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n")
            # Fill in end.
# Close the client and the server sockets
# Fill in start.
tcpCliSock.close()
# Fill in end.
