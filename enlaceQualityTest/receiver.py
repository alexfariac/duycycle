import socket
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 12000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT)) 

revc = 0
total = 1
while 1:
	data, addr = sock.recvfrom(1024)
	data = json.loads(data.decode())
	print(data)

	if data['done']:
		eq = (revc/total)*100
		data = {"eq": eq, "revc": revc}
		data = json.dumps(data).encode()
		sock.sendto(data, addr)
		
		revc = 0
		total = 1
	else:
		total = data['total']
		revc+=1


eq = (revc/total)*100
print("RECEIVED {} OUT OF {} PACKAGES".format(revc, total))
print("LINK QUALITY : {}%".format(eq))