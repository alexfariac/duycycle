import socket
import time
import os

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP) # UDP


i = 0
print(range(15))
for x in range(15):
	try:
		time.sleep(0.001)

		if(x == 5):
			os.system("ifconfig wlp3s0 down")


		if(x == 10):
			os.system("ifconfig wlp3s0 up")


		sock.sendto(str(i), (UDP_IP, UDP_PORT))

	except Exception as e:
		pass

	finally:
		i = i+1
	


