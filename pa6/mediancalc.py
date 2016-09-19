# Copyright AN. December 2015
#!/usr/bin/python -tt
# Heap Data Structure
# Source : https://youtu.be/v1YUApMYXO4

import math
import random
from heap import *
import sys

def main():

  if len(sys.argv) < 2:
    print 'usage: ./mediancalc.py --filename'
    sys.exit(1)
  
  arr = []
  filename = sys.argv[1] # This argument has filename argument
  print filename
  with open(filename) as f:
    for line in f:
        data = line.split()
        arr.append(int(data[0]))
    

  #arr = [67,78,62,64,69,61,0,58,41,5,24,45,27,34,81]
  #arr = [1,2,3]
  #arr = [1,2,3,4,5,6]
  heaplow = []
  heaphigh = []
  median = 0
  #print arr
  count = 0
  medianlog = []
  
  for x in arr:
	#negheaphigh = [ -x for x in heaphigh]
	#print median,heaplow,heaphigh
	if abs(x) < median:
		AddElement(heaplow,x)
	else:
		AddElement(heaphigh,-x)
	
	#print "dbg",heaplow,heaphigh
	count = count + 1
	
	# Balance the heap sizes
	if len(heaplow) - len(heaphigh) > 1:
		AddElement(heaphigh,-heaplow[0])
		heaplow = RmElement(heaplow)
	elif len(heaphigh) - len(heaplow) > 1:
		AddElement(heaplow,-heaphigh[0])
		heaphigh = RmElement(heaphigh)
		#print "inside",heaplow,heaphigh
	
	if count%2 == 0: #even
		median = heaplow[0]
		medianlog.append(median)
	else:
		if len(heaplow) > len(heaphigh): #odd
			median = heaplow[0]
			medianlog.append(median)
		else:
			median = abs(heaphigh[0])
			medianlog.append(median)
	#print "Here",heaplow,heaphigh,count
  #print heaplow,heaphigh
  print sum(medianlog)%10000
  #arr.sort()
  #print arr

if __name__ == '__main__':
  main()

