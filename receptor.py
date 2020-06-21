import socket
import time
import subprocess
import sys
import random

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.setblocking(0) #set the sock to do nonbloking read operations

sock.bind((UDP_IP, UDP_PORT)) #bind the socket to the port and addr 

#python3 tranmissor.py {{reps}} {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
args = sys.argv[1:7]

INTERFACE, SLOT_SIZE, P, METHOD = args[0:4] 
dutyCicleArgs = args[4:7]

args = ['python3','schedule.py', INTERFACE, SLOT_SIZE, METHOD]+dutyCicleArgs

#this calls the duty cicle method using the parameters we passed
#INTERFACE SLOT_SIZE DUTY_CICLE_METHOD DUTY_CICLE_PARAMS
subprocess.Popen(args)

P = int(P)/100
while True:

	try:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    if data:

	    	r = random.random() #0.0 to 1.0
	    	#P should be from 0 to 100 inclusive. 
	    	recvPkg = r <= P #if the random number is smaller than or equal to the enlace quality operator, then the package would have benn received

	    	print("Received: ", data, P, r)

	    	if recvPkg:
		    	#enviar de volta a mensagem com o valor recebido, para o endereco e porta 
		    	sock.sendto(data, addr)

	except Exception as e:
		#In case of exceptions we just pass, many exceptions are raised by expecteded behavirous
		#Such as  #BlokingIOError: Errno 11 and HostUnrecheables
		pass