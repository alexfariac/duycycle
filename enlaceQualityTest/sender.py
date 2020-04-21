import socket
import json


UDP_IP = '127.0.0.1'
UDP_PORT = 12000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

SENDS = 100

for rep in range(SENDS):
	datagram = {'no': rep, 'total': SENDS, 'done':0}
	datagram = json.dumps(datagram).encode()

	sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data

while 1:
	datagram = {'done':1}
	datagram = json.dumps(datagram).encode()
	sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data	