import os
import time
from random import randint

#function to create a matrix of arbitrary size
def createGrid(lines, columns, upLine, upColumn):
	if(lines <= 0 or columns <= 0 or upLine > lines or upColumn > columns): 
		return 0
	else:
		#for line or column with given index (first in this case) we set the value for 1
		return [1 if (x == upLine or y == upColumn) else 0 for x in range(lines) for y in range(columns)]
		
def main():

	slotSize = 200; #size of the schedule slot in ms

	schedule = createGrid(4,5, randint(0,3), randint(0,4))

	scheduleIndex = 0

	while True:

		print(scheduleIndex, schedule[scheduleIndex])
		time.sleep(slotSize/1000)


		#while not at the end of the schedule indexes we increment the couter, else we refresh i
		scheduleIndex = 0 if scheduleIndex >= len(schedule)-1 else scheduleIndex+1

	# print("START", time.strftime("%Y/%m/%d, %H:%M:%S"))
	# os.system("rfkill block 1")
	# os.system("rfkill unblock 1")
	# print(stream.read())
	# return 0


# a = createGrid(4,5, 0, 2)
# print(a)
main()