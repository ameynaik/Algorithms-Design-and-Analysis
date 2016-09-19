# Copyright AN. August 2016
#!/usr/bin/python -tt

import sys
import random
import time
from quick_sort import *


def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    foundit = False
	
	    while first<=last and not foundit:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            foundit = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	
	    return foundit
	 
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
  print sorted_array[len(array)/2]
  
  data = sorted_array
  '''
  thefile = open('test.txt', 'w')
  for item in sorted_array:
	thefile.write("%s\n" % item)
  '''

  start = 0
  end = len(sorted_array)-1
  MIN = -10000
  MAX = 10000
  i = 0
  '''
  for i in range(-MIN,MAX+1):
	found[i] = 0;
	i = i + 1
  '''
  found = [0]*(MAX-MIN+1)
  
  while (start < end):
        probe_sum = data[start] + data[end];
        if (probe_sum < MIN):
            # the value is too small, there is just no hope for success, let go the small side
            start = start +1
			
        elif (probe_sum > MAX):
            # the value is too large, there is just no hope for success, let go the small side
            end = end -1
        else:
            if (data[start] != data[end]):
                found[probe_sum - MIN] = 1;
            current_start = start;
            current_end = end;
            while (1):
				#let see if there are any more solution starting with the same end
                start = start +1
                probe_sum = data[start] + data[end];
                if (probe_sum < MIN):
                    # This is impossible
                    break;
                elif (probe_sum > MAX):
                    break;
                else:
                    if (data[start] != data[end]):
                        found[probe_sum - MIN] = 1;
            start = current_start;

            while (1):
                # let see if there are any more solution starting with the same start
                end = end -1
                probe_sum = data[start] + data[end];
                if (probe_sum < MIN):
                    break;
                elif (probe_sum > MAX):
                    # This is impossible
                    break;
                else:
                    if (data[start] != data[end]):
                        found[probe_sum - MIN] = 1;
            end = current_end;
            # We have exhausted all solution with start and end, so skip them both
            start = start + 1
            end = end -1
	# count = 0;
    # for i in range(MIN,MAX+1):
        # if (found[i - MIN]):
            # count = count + 1

  print found.count(1)
  

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))