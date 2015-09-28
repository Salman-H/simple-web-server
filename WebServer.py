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
