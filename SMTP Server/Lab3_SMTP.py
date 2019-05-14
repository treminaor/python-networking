import socket
import base64

msg = b'\r\n Ahmed Banafa is the best'
endmsg = b'\r\n.\r\n'

sender = b'<from@smtp.mailtrap.io>'
recipient = b'<to@smtp.mailtrap.io>'
username = b'2ea92799a82d0f'
password = b'0e9b519ff2c27d'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.mailtrap.io'
port = 2525

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket.socket()
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024)
print('Establish TCP connection with mailserver')
print (recv)
if recv[:3] != b'220':
	print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = b'HELO mailtrap.io\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print('Send HELO command')
print (recv1)
if recv1[:3] != b'250':
	print ('250 reply not received from server.')

# Send the AUTH LOGIN command and print server response.
authCommand = b'AUTH LOGIN\r\n'
clientSocket.send(authCommand)
auth_recv = clientSocket.recv(1024)
print('Auth with server')
print (auth_recv)
if auth_recv[:3] != b'334':
	print ('334 reply not received from server')

# Send username and print server response.
uname = base64.b64encode(username) + b'\r\n'
clientSocket.send(uname)
uname_recv = clientSocket.recv(1024)
print('Send username')
print('sending ', uname, ' to server')
print (uname_recv)
if uname_recv[:3] != b'334':
	print ('334 reply not received from server')

# Send password and print server response.
pword = base64.b64encode(password) + b'\r\n'
clientSocket.send(pword)
pword_recv = clientSocket.recv(1024)
print('Send password')
print('sending ', pword, ' to server')
print (pword_recv)
if pword_recv[:3] != b'235':
	print ('235 reply not received from server')

# Send MAIL FROM command and print server response.
mailFromCommand = b'MAIL FROM: ' + sender + b'\r\n'
clientSocket.send(mailFromCommand)
recv2 = clientSocket.recv(1024)
print('Send MAIL FROM')
print(mailFromCommand)
print (recv2)
if recv2[:3] != b'250':
	print ('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = b'RCPT TO: ' + recipient + b'\r\n'
clientSocket.send(rcptToCommand)
recv3 = clientSocket.recv(1024)
print('Send RCPT TO')
print (recv3)
if recv3[:3] != b'250':
	print ('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = b'DATA\r\n'
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print('Send DATA')
print (recv4)
if recv4[:3] != b'354':
	print ('354 reply not received from server.')

# Send message data.
clientSocket.send(msg)

# Message ends with a single period.
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print (recv5)
if recv5[:3] != b'250':
	print ('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = b'QUIT\r\n'
clientSocket.send(quitCommand)
recv6 = clientSocket.recv(1024)
print (recv6)
if recv6[:3] != b'221':
	print ('221 reply not received from server.')

clientSocket.close()
