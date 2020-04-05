import socket
import time

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# sock.setblocking(0)

sock.bind((UDP_IP, UDP_PORT))

while True:
	try:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    if data:
	    	print("received message:", data)
	    	#enviar de volta a mensagem com o valor recebido
	    	sock.sendto(str(data).encode(), ("192.168.1.1", 5000))

	    else:
	    	print("No data yet")

	except Exception as e:
		print(e)