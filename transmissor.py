import socket
import time
import sys
import subprocess
import json
import random
from dutyCicle import Schedule

UDP_IP = "192.168.1.2"
UDP_PORT = 5000

sock_addr = (UDP_IP, UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM, # UDP
                     socket.IPPROTO_UDP) 

#set the socket to nonblockable
sock.setblocking(0)

# sock.bind((UDP_IP, UDP_PORT))


#python3 tranmissor.py {{reps}} {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
args = sys.argv[1:7]

REPS = int(args[0]) #Number of tests to be performed, each test should only have one successfull send/receiveback
INTERFACE, SLOT_SIZE, METHOD = args[1:4] 
dutyCicleArgs = args[4:7]

args = ['python3','schedule.py', INTERFACE, SLOT_SIZE, METHOD]+dutyCicleArgs

method = "{}({})".format(METHOD.lower(), ",".join(dutyCicleArgs) )
schedule_obj = Schedule(method)
scheduleSize = schedule_obj.getSize()
# scheduleSize = schedule_obj
	

# i=0 #Noof slots runned so far
responses = {}
for rep in range(REPS): #repeat the test multiple times

	# duty_cicle = subprocess.Popen(['python3', 'schedule.py', 'wlp3s0', '200', 'grid', '4', '4'])
	#this calls the duty cicle method using the parameters we passed
	duty_cicle = subprocess.Popen(args)
	#INTERFACE SLOT_SIZE DUTY_CICLE_METHOD DUTY_CICLE_PARAMS

	slotDelay = random.randint(0,scheduleSize-1)
	print("Waiting {} slots for test {}".format(slotDelay, rep))
	testDelay = (slotDelay*int(SLOT_SIZE))/1000
	time.sleep(testDelay)

	i=0
	while 1:
		try:

			# data_to_send = "TestNo {}, SlotNo {}".format(rep, i).encode() #prepare data for sending
			data_to_send = json.dumps({'TestNo':rep, 'SlotNo':i}).encode()
			sock.sendto(data_to_send, (UDP_IP, UDP_PORT)) #send the data 
			
			#we check (assinc) if we received data back from the receiver, was this the slot that had communication? 
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
			data = json.loads(data.decode())

			if data and data["TestNo"] == rep :
				#we received back data from receiver so there was successfull comunicatioin therefor we can prepare to set a new round of test
				#reset parameters for new test
				print("	{}".format(data))
				responses[data["TestNo"]] = data["SlotNo"]
				duty_cicle.terminate() #end the subprocess that is running the current duty cicle so we can start a new one for next test
				break #we get out the the index count loop, and go back to the tests repetitions loop

		except BlockingIOError as IOException:
			#This exception is throw usually when we have no data wet to receive
			#setbloking(0) has this behaviour
			# print("No data to receive yet")
			pass

		except OSError as OSException:
			# This exception is throw when the host is unrecleable, mostly because our interface is down
			# print(OSException, "Interface down")
			pass
	
		finally:
			i = i+1
			time.sleep(int(SLOT_SIZE)/1000) #wait for the slot time #we only try to send once each slot

print("--------------------------")
print(responses, len(responses))
s = sum(responses.values())
l = len(responses)
a = s/l
print(s,l,a)

