# Copyright AN. August 2016
#!/usr/bin/python -tt

import sys
import random
import time
from quick_sort import *


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
	 
def main():
  if len(sys.argv) < 2:
    print 'usage: ./TwoSumProblem.py --filename'
    sys.exit(1)
  
  array = []
  count = 0
  filename = sys.argv[1] # This argument has filename argument
  print filename
  with open(filename) as f:
    for line in f:
        data = line.split()
        array.append(int(data[0]))
    
  #print array
  sorted_array = quick_sort_func(array)
  print len(array)
  print len(sorted_array)
  #print sorted_array[1:100]
  for t in range(-10000,10001):
	print "I am here"
	for x in sorted_array:
		if (binarySearch(sorted_array,t-x)):
			if (x != t-x):
				count = count + 1
				print count,t
			break

  print count

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))