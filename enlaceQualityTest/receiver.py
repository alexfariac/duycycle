import socket
import json

UDP_IP = "192.168.1.2"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))


revc = 0
total = 1
while 1:
	data, addr = sock.recvfrom(1024)
	data = json.loads(data.decode())

	if data['done']:
		break

	if data:
		total = data['total']
		revc+=1

	print(data)

eq = (revc/total)*100
print("RECEIVED {} OUT OF {} PACKAGES".format(revc, total))
print("LINK QUALITY : {}%".format(eq))