import socket
import time
import os

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP) # UDP


i = 0
for x in range(100):
	try:
		time.sleep(1)


		sock.sendto(str(i), (UDP_IP, UDP_PORT))
		print(str(i))

	except Exception as e:
		print(e)
		pass

	finally:
		i = i+1
	


