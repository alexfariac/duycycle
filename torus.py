import sys
import os
import time
from random import randint

#function to create a matrix of arbitrary size
def createSchedule(lines, columns, upLine, upColumn):
	if(lines <= 0 or columns <= 0 or upColumn > columns): 
		return 0
	else:
		matrix = [[1 if ( (lin == upLine and col < (columns//2)+1) or col == upColumn) else 0 for col in range(columns)] for lin in range(lines)]
		schedule = []
		for line in matrix:
			schedule += line
		return schedule

def main():

	slotSize = 5000; #size of the schedule slot in ms
	lines = columns = 4
	interace="wlp3s0"
	schedule = createSchedule(lines, columns, 0, 0)

	scheduleIndex = 0

	print("START", time.strftime("%Y/%m/%d, %H:%M:%S")) #start of the schedule
	while True:

		if(schedule[scheduleIndex]):
			#interface on
			print("Interface  ON", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} up".format(interface))
		else:
			#interfaceoff
			print("Interface  OFF", time.strftime("%H:%M:%S"))
			os.system("ifconfig {} down".format(interface))



		#while not at the end of the schedule indexes we increment the couter, else we refresh i
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1

		#we now wait for the slottime to end
		time.sleep(slotSize/1000)

	return 0


main()