import socket
import time
import shlex
import subprocess

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

#set the socket to nonblockable
sock.setblocking(0)

# sock.bind((UDP_IP, UDP_PORT))

i=0 #numero de slots percorridos até o momento
reps = 5 #quantidade de repeticoes de testes
slot_size = 1000 #tamanho em MS de cada slot
for rep in range(reps): #repeat the test multiple times

	duty_cicle = subprocess.Popen(['python3', 'schedule.py', 'wlp3s0', '1000', 'grid', '4', '4'])
	##python3 schedule.py wlp3s0 100 grid 4 4 #exemple call

	while 1:
		try:
			time.sleep(int(slot_size)/1000) #wait for the slot time #we only try to send once each slot

			data_to_send = str(i).encode()
			sock.sendto(data_to_send, (UDP_IP, UDP_PORT))
			
			#Espera retorno do receptor (foi esse o slot em que houve comunicacao ?)
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

			if data:
				#recebemos retorno do receptor com o valor do primeiro slot de comunicacao
				#resetar os parametros para um novo teste
				i = 0 #setar o contador paraum valor aleatorio dentro do schedule
				print("RECEIVED BACK: TESTno {}, SLOTno {}".format(rep,data))
				duty_cicle.terminate() #terminar o duty cicle atual. 
				break #we get out the the index count loop, and go back to the tests repetitions loop


		except Exception as e:
			#when conection is unreachable
			# print(e)
			pass

		finally:
			i = i+1
	


