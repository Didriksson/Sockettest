import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('DIDDE-DATOR', 9090)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	message = "Testing Testing. Just do me a Hello World!"
	print "Sending message."
	sock.sendall(message)
	
	amount_received = 0
	amount_excepcted = len(message)
	
	while amount_received<amount_excepcted:
		data = sock.recv(100)
		amount_received += len(data)
		print "Received: "+ data
finally:
	sock.close()
	
	