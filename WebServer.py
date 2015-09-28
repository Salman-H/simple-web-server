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
