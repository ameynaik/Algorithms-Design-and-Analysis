# Copyright AN. January 2016
#!/usr/bin/python -tt

# Quick Sort Algorithm
# Source : https://www.youtube.com/watch?v=y_G9BkAm6B8


import sys
import random
import time
start_time = time.time()
inv_count = 0
comp_count = 0
pivot_position = 2 # 0 - first, 1 - last, 2 - median

def quick_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	partition(array,0,len_of_array-1,pivot_position)
	return array

def median_calc(array,first,last): # Array contains array to be sorted.
	med = first + ((last-first) >> 1)
	if (array[first] > array[med] and array[first] < array[last]) or (array[first] < array[med] and array[first] > array[last]) :
		pivot_pos = first
	elif (array[med] > array[first] and array[med] < array[last]) or (array[med] < array[first] and array[med] > array[last]):
		pivot_pos = med
	else:
		pivot_pos = last
	
	#print "first,med,last",first,med,last,pivot_pos
	#print "array[f,m,l]",array[first],array[med],array[last]
	return pivot_pos
	
	
	
def partition(array,first,last,pivot_position):
	global inv_count
	global comp_count
	size = last-first+1
	
	comp_count = comp_count + size - 1 
	subarr = array[first:last+1]
	
	if(size < 2):
		return array
	
	if (pivot_position == 0):
		pivot = subarr[0] #subarr[random.randint(1, 1000000)%size]
	elif (pivot_position == 1):
		pivot = subarr[-1]
		subarr[0],subarr[-1] = subarr[-1],subarr[0]
	else:
		pivot_pos = median_calc(array,first,last)
		pivot = subarr[pivot_pos - first]
		subarr[0],subarr[pivot_pos - first] = subarr[pivot_pos - first],subarr[0]
	
	L = 0
	U=size-1
	#print "pivot : ",pivot
	#print "partition called :",subarr,first,last,size,comp_count,pivot
	i = first+1;
	#print range(1,size)
	for j in range(1,size):
		#print "here",subarr[j],pivot
		if subarr[j] < pivot:
			#print "subarr (i-first,j) ",subarr[j],subarr[i-first]
			subarr[i-first],subarr[j] = subarr[j],subarr[i-first]
			i += 1
	#print "subarr (first,i-1) ",subarr,first,i-1,pivot
	subarr[first-first],subarr[i-1-first] = subarr[i-1-first],subarr[first-first]

	#print "L & U value : ",L,U
	array[first:last+1] = subarr
	#print "Subarr at the end of routine : ",subarr
	#if (L-1+first > first):
	if (i-2 > first):
		#print "subarr is :",array[first:i-1]
		partition(array,first,i-2,pivot_position)
	
	#print "last,i ",last,i
	if (last > i):
		#print "here"
		#print "subarr is :",array[i:last+1]
		partition(array,i,last,pivot_position)
	
	return array

	
	
	
		 
def main():
  if len(sys.argv) < 2:
    print 'usage: ./quick_sort.py --filename'
    sys.exit(1)
  
  array = []
  filename = sys.argv[1] # This argument has filename argument
  print filename
  with open(filename) as f:
    for line in f:
        data = line.split()
        array.append(int(data[0]))
    
  #print array
  # Create Random numbers of this length. The random numbers generated are unique.
  #array = random.sample(xrange(10), int(len_of_array))
  #print "This is the input array"
  #print array
  #array = [9,3,4,2,1,7,5,6,8,10]
  #array = [1,2,3,4,5,6]
  #array = [6,5,4,3,2,1]
  #array = [3,4,2]
  sorted_array = quick_sort(array)
  #print sorted_array
  print "inv_count : ", inv_count
  print "comp_count: ", comp_count
  print len(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))