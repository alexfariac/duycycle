import os
import sys
import time
from random import randint

def createSchedule(p, q):
	return [1 if slot%q == 0 or slot%p == 0 else 0 for slot in range(p*q)] 


def main():

	slotSize = 5000; #size of the schedule slot in ms
	p = 3
	q = 5

	schedule = createSchedule(p,q)
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
