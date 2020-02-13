import os
import sys
import time
from random import randint

#function to create a matrix of arbitrary size
def createGrid(lines, columns, upLine, upColumn):
	if(lines <= 0 or columns <= 0 or upLine > lines or upColumn > columns): 
		return 0
	else:
		#for line or column with given index (first in this case) we set the value for 1
		return [1 if (lin == upLine or col == upColumn) else 0 for col in range(columns) for lin in range(lines)]
		
def main():

	slotSize = 5000; #size of the schedule slot in ms
	lines = columns = 4

	schedule = createGrid(lines, columns, randint(0,lines-1), randint(0,columns-1))
	print(schedule)
	
	scheduleIndex = 0

	print("START", time.strftime("%Y/%m/%d, %H:%M:%S")) #start of the schedule
	while True:

		if(schedule[scheduleIndex]):
			#interface on
			print("Interface  ON", time.strftime("%H:%M:%S"))
			os.system("ifconfig wlp3s0 up")
		else:
			#interfaceoff
			print("Interface OFF", time.strftime("%H:%M:%S"))
			os.system("ifconfig wlp3s0 down")



		#while not at the end of the schedule indexes we increment the couter, else we refresh i
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1

		#we now wait for the slottime to end
		time.sleep(slotSize/1000)

	return 0


main()