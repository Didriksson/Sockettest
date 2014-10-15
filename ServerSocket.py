import sys
import socket
from thread import *

HOST = ''
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((socket.gethostname(), PORT))
except socket.error as msg:
	print "Coult not bind to hostname. Error code: " +  str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	
print "Socket bind complete."
s.listen(10)
print "Socket now listening."

def clientthread(conn):
	conn.send("Welcome! This is the server speaking!")
	while True:
		data = conn.recv(1024)
		repy = "OK..." + data
		if not data:
			break;

	conn.close()
	
	
while True:
	conn, addr = s.accept()
	print "Connected with " + str(addr[0]) +":"+str(addr[1])
	
	start_new_thread(clientthread, (conn,))
s.close()