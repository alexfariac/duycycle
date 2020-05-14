#HOW TO CALL THIS METHOD MORE INFO AT MAIN METHOD DEFINITION
#python schedule.py {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
import os
import sys
import time
import random
from dutyCicle import Schedule


def main():
	#eg. python schedule.py wlp3s0 1000 grid 4 4
	#python schedule.py {{interface}} {{slot_size}} {{duty_cicle_method}} {{duty_cicle_args}}
	#interface = the interface that should use your duty cicle
	#slot_size = the size of the slot in duty cicle (the amount of time in MS until move to the next slot)
	#duty_cicle_args should be passed one by one separete by space
	
	args = sys.argv[1:6]

	interface, slotSize, dutyCicleMethod = args[0:3]
	dutyCicleArgs = ",".join(args[3:6])

	method = "{}({})".format(dutyCicleMethod.lower(), dutyCicleArgs )
	
	schedule_obj = Schedule(method)
	
	schedule = schedule_obj.schedule
	scheduleIndex = random.randint(0, schedule_obj.getSize()-1) #we start the 

	# print("START", time.striftime("%Y/%m/%d, %H:%M:%S")) #start of the schedule
	while True:

		if(schedule[scheduleIndex]):
			#interface on
			# print("Interface  ON", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} up".format(interface))
		else:
			#interfaceoff
			# print("Interface  OFF", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} down".format(interface))



		#while not at the end of the schedule indexes we increment the couter, else we refresh i
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1

		#we now wait for the slottime to end
		time.sleep(int(slotSize)/1000)

	return 0


main()

