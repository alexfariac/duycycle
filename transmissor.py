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

i=0 #Noof slots runned so far
reps = 100 #Number of tests to be performed, each test should only have one successfull send/receiveback
slot_size = 200 #size of duty cicle slot in MS

for rep in range(reps): #repeat the test multiple times

	#this calls the duty cicle method using the parameters we passed
	#INTERFACE SLOT_SIZE DUTY_CICLE_METHOD DUTY_CICLE_PARAMS
	# duty_cicle = subprocess.Popen(['python3', 'schedule.py', 'wlp3s0', '2000', 'grid', '4', '4'], creationflags = subprocess.CREATE_NEW_CONSOLE)
	duty_cicle = subprocess.Popen(['python3', 'schedule.py', 'wlp3s0', '200', 'grid', '4', '4'])
	##python3 schedule.py wlp3s0 100 grid 4 4 #exemple call

	while 1:
		try:
			time.sleep(int(slot_size)/1000) #wait for the slot time #we only try to send once each slot

			data_to_send = "TestNo {}, SlotNo {}".format(rep, i).encode() #prepare data for sending
			sock.sendto(data_to_send, (UDP_IP, UDP_PORT)) #send the data 
			
			#we check (assinc) if we received data back from the receiver, was this the slot that had communication? 
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

			if data:
				#we received back data from receiver so there was successfull comunicatioin therefor we can prepare to set a new round of test
				#reset parameters for new test
				i = 0 #clear the counter that checks how many slots have passed so far
				print("RECEIVED BACK: {}".format(data))
				duty_cicle.terminate() #end the subprocess that is running the current duty cicle so we can start a new one for next test
				break #we get out the the index count loop, and go back to the tests repetitions loop


		except Exception as e:
			#when conection is unreachable #INTERFACE OFF
			#when resource is busy/unavailable #NO DATA YET
			# print(e)
			pass

		finally:
			i = i+1
	


