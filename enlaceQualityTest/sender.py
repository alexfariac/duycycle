import socket
import json
import time	


UDP_IP = '192.168.1.2'
UDP_PORT = 12000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

sock.setblocking(0)

SENDS = 1000

for rep in range(SENDS):
	datagram = {'no': rep, 'total': SENDS, 'done':0}
	datagram = json.dumps(datagram).encode()

	print("Sending: {}".format(datagram))
	sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data

	#adicionar intervalo 100ms
	time.sleep(0.1)

while 1:
	try:
		datagram = {'done':1}
		datagram = json.dumps(datagram).encode()
		sock.sendto(datagram, (UDP_IP, UDP_PORT)) #send the data	

		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		data = json.loads(data.decode())

		if data:
			print("REVEIVED BACK")
			print(data)
			break;

	except Exception as e:
		pass
