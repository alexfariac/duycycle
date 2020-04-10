import select
import socket
import sys
import time
import os

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

#set the socket to nonblockable
sock.setblocking(0)

# sock.bind((UDP_IP, UDP_PORT))

reps = 1000
slot_size = 1000

for n in range(reps): #repeat the test multiple times
	running_test = True #we reset the test control parameter
	i = 0 #setar o contador paraum valor aleatorio dentro do schedule


	while running_test:
		try:
			time.sleep(int(slot_size)/1000) #wait for the slot time #we only try to send once each slot

			data_to_send = str(i).encode()
			sock.sendto(data_to_send, (UDP_IP, UDP_PORT))
			
			#Espera retorno do receptor (foi esse o slot em que houve comunicacao ?)
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

			if data:
				#recebemos retorno do receptor com o valor do primeiro slot de comunicacao
				#resetar os parametros para um novo teste
				# i = 0
				print("RECEIVED", data)


		except Exception as e:
			#when conection is unreachable
			print(e)
			pass

		finally:
			i = i+1
	


