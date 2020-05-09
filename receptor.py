import socket
import time
import subprocess
import sys
import os
import random
from schedule import Schedule

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, # Internet
					 socket.SOCK_DGRAM) # UDP

sock.setblocking(0) #set the sock to do nonbloking read operations

sock.bind((UDP_IP, UDP_PORT)) #bind the socket to the port and addr 

#python3 tranmissor.py {{reps}} {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
args = sys.argv[1:6]

INTERFACE, SLOT_SIZE, METHOD = args[0:3] 
# dutyCicleArgs = args[3:6]

dutyCicleArgs = ",".join(args[3:6])

method = "{}({})".format(METHOD.lower(), dutyCicleArgs )

schedule_obj = Schedule(method)

schedule = schedule_obj.schedule
scheduleIndex = random.randint(0, schedule_obj.getSize()-1) #we start the 

#this calls the duty cicle method using the parameters we passed
#INTERFACE SLOT_SIZE DUTY_CICLE_METHOD DUTY_CICLE_PARAMS
# subprocess.Popen(args)

while True:
	try:
		if(schedule[scheduleIndex]):
			#interface on
			print("Interface  ON", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} up".format(INTERFACE))
		else:
			#interfaceoff
			print("Interface  OFF", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} down".format(INTERFACE))
		
		
		data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
		if data:
			print("Received: ", data)
			#enviar de volta a mensagem com o valor recebido, para o endereco e porta 
			sock.sendto(data, addr)

	except Exception as e:
		#In case of exceptions we just pass, many exceptions are raised by expecteded behavirous
		#Such as  #BlokingIOError: Errno 11 and HostUnrecheables
		pass
	finally:
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1
		time.sleep(int(SLOT_SIZE)/1000) #wait for the slot time #we only try to send once each slot
		pass