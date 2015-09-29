#!/usr/bin/env python

from socket import *

# Create a server TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare server socket

serverHost = 'localHost'
recvBuffer = '1024'			# receive buffer
serverPort = 12000			# Port number

# Bind the serverSocket to port 12000
serverSocket.bind(('',serverPort))
										
# serverSocket will Listen to one connection at a time
# i.e. the max number of queued connections is 1
serverSocket.listen(1)

print 'The server is ready to receive'

while True:
	# Establish the connection
	print 'Ready to serve...'

	# Create a client TCP socket
	# Connection socket will be created when
	# contacted by a client (browser)
	connectionSocket, addr = serverSocket.accept()

	try:
		# Receive the HTTP request from this connection
		message = connectionSocket.recv(1024)	# The connection has received the
												# message from 1024, or the client

		filename = message.split()[1]
		f = open(filename[1:])
		
		# Read the file and 
		# store its contents in outputdata
		outputdata = f.read()
		
		# Send HTTP Response Status line into the socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
														
		# Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		
		# Close client socket
		connectionSocket.close()
