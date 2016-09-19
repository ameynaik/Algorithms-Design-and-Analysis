# Copyright AN. August 2016
#!/usr/bin/python -tt

import sys
import random
import time

def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found

def hashfunc(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False
	
	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return found
	 
def main():
  if len(sys.argv) < 2:
    print 'usage: ./hashing.py --filename'
    sys.exit(1)
  
  array = []
  count = 0
  HT = {}
  filename = sys.argv[1] # This argument has filename argument
  print filename
  with open(filename) as f:
    for line in f:
        data = line.split()
        array.append(int(data[0]))
    
  #print array
  #pw = 1523 #
  pw = 5531 #10007
  for i in range(0,pw):
	HT[i] = []
  
  for x in array:
	HT[x%pw].append(x)  
  
  max_bucket = 0
  for i in range(0,pw):
	if (len(HT[i]) > max_bucket):
		max_bucket = len(HT[i])
	  
  print max_bucket
  
  count  = 0
  
  for t in range(-10000,10001):
	for x in array:
		if (binarySearch(HT[(t-x)%pw],t-x)):
			if (x != t-x):
				count = count + 1
				print count,t
			break

  print count
  

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))