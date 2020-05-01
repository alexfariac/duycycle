import os
import sys
import time
import random

class Schedule:

	def __init__(self, method):
		self.schedule = eval("self."+method) #the schedule array

	def getSize(self):
		return len(self.schedule)

	def torus(self, lines,columns, upLine = 0, upColumn = 0):
		if(lines <= 0 or columns <= 0 or upColumn > columns): 
			raise Exception ("Array invalid offset for line os columns")
		else:
			matrix = [[1 if ( (lin == upLine and col < (columns//2)+1) or col == upColumn) else 0 for col in range(columns)] for lin in range(lines)]
			schedule = []
			for line in matrix:
				schedule += line
			return schedule

	def grid(self, lines, columns, upLine = 0, upColumn = 0):
		if(lines <= 0 or columns <= 0 or upLine > lines or upColumn > columns): 
			raise Exception ("Array invalid offset for line os columns")
		else:
			#for line or column with given index (first in this case) we set the value for 1
			return [1 if (lin == upLine or col == upColumn) else 0 for col in range(columns) for lin in range(lines)]

	def searchlight(self, t, *_):
		return [1 if slot == 0 or slot == row+1 else 0 for row in range(t//2) for slot in range(t)] 

	def disco(self, p,q):
		return [1 if slot%q == 0 or slot%p == 0 else 0 for slot in range(p*q)] 

	def blockdesign(self, k, *_):
		f = open("./blockdesigns", "r") #read the file that has our preprocessed blockdesigns
		content = f.readlines()
		for line in content:
			line_array = line.strip("\n").split(",") #for eachline make an array with our info
			
			if line_array[1] == str(k):

				active_slots = line_array[3:] #get the subarray of active slots in the duty_cicle
				print(active_slots)
				schedule = [0]*int(line_array[0]) #create array of size v with all zeros
				for on in active_slots: #for each on index in the duty_cicle turn on the acctual schedule array
					schedule[int(on)] = 1

				f.close()
				return schedule
		
		f.close()			
		raise Exception ("k parameter {} invalid".format(k))

def main():
	args = sys.argv[1:6]
	dutyCicleMethod = args[0]
	dutyCicleArgs = ",".join(args[1:4])

	method = "{}({})".format(dutyCicleMethod.lower(), dutyCicleArgs )

	schedule_obj = Schedule(method)

	schedule = schedule_obj.schedule
	onIndexs = sum(schedule)

	print(schedule)
	dc = (onIndexs*100.0/len(schedule))
	print(dc,"%")


main()