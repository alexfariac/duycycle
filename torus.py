import sys
import os
import time
from random import randint

#function to create a matrix of arbitrary size
def createSchedule(lines, columns, upColumn):
	if(lines <= 0 or columns <= 0 or upColumn > columns): 
		return 0
	else:
		return [1 if (lin == upLine or x == upColumn) else 0 for col in range(columns) for y in range(lines)]
		#now we fill the rows

a = (createSchedule(4,4,2))
for line in a:
	print(line)