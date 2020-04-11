import socket
import time
import subprocess

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.setblocking(0) #set the sock to do nonbloking read operations

sock.bind((UDP_IP, UDP_PORT)) #bind the socket to the port and addr 

#python3 tranmissor.py {{reps}} {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
args = sys.argv[1:7]

REPS = args[0] #Number of tests to be performed, each test should only have one successfull send/receiveback
INTERFACE, SLOT_SIZE, METHOD = args[1:4] 
dutyCicleArgs = args[4:7]

args = ['python3','schedule.py', INTERFACE, int(SLOT_SIZE), METHOD]+dutyCicleArgs

#this calls the duty cicle method using the parameters we passed
#INTERFACE SLOT_SIZE DUTY_CICLE_METHOD DUTY_CICLE_PARAMS
subprocess.Popen(args)

while True:
	try:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    if data:
	    	print("Received: ", data)
	    	#enviar de volta a mensagem com o valor recebido, para o endereco e porta 
	    	sock.sendto(str(data).encode(), addr)

	except Exception as e:
		#In case of exceptions we just pass, many exceptions are raised by expecteded behavirous
		#Such as  #BlokingIOError: Errno 11 and HostUnrecheables
		pass