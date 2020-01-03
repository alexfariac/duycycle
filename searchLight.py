import os
import sys
import time
from random import randint

def createSchedule(t):
	return [1 if slot == 0 or slot == row+1 else 0 for row in range(t/2) for slot in range(t)] 


def main():

	slotSize = 5000; #size of the schedule slot in ms

	schedule = createSchedule(4)
	print(schedule)
	
	scheduleIndex = 0

	print("START", time.strftime("%Y/%m/%d, %H:%M:%S")) #start of the schedule
	while True:

		if(schedule[scheduleIndex]):
			#interface on
			print("Interface  ON", time.strftime("%H:%M:%S"))
			os.system("rfkill unblock 1")
		else:
			#interfaceoff
			print("Interface OFF", time.strftime("%H:%M:%S"))
			os.system("rfkill block 1")



		#while not at the end of the schedule indexes we increment the couter, else we refresh i
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1

		#we now wait for the slottime to end
		time.sleep(slotSize/1000)

	return 0


main()
