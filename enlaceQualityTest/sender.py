import socket
import json


UDP_IP = '192.168.1.2'
UDP_PORT = 12000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

SENDS = 100000

for rep in range(SENDS):
	datagram = {'no': rep, 'total': SENDS, 'done':0}
	datagram = json.dumps(datagram).encode()

	print("Sending: {}".format(datagram))
	sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data

for x in range(100):
	datagram = {'done':1}
	datagram = json.dumps(datagram).encode()
	sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data	