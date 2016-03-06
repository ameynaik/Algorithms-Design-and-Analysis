# Copyright Amey Naik. Feb 2016
#!/usr/bin/python -tt

# Algorithms: Design and Analysis, Part 1
# Programming Assignment 1.
# merge Sort Algorithm + Counts the number of inversions
# Source : https://www.youtube.com/watch?v=GCae1WNvnZM


import sys
import random
import time
start_time = time.time()
cnt_inv = 0 #Variable to count number of inversions

def merge_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	i = 1
	level = 1
	while i < len_of_array:
		j = 0
		while j<len_of_array-i:
			sort_and_merge(array,level,j)
			j = j+2*i
		i = 2*i
		level = level + 1
	return array
	
def sort_and_merge(array,level,j):
	global cnt_inv
	n = 2**(level) #Output Length of merged array.
	a = array[j:j+(n/2)]
	b = array[j+(n/2):j+n]
	c =[None]*n
	x = 0
	y = 0
	for k in range(0,n):
		if x >= len(a):
			c[k:n] = b[y:(n/2)]
			break
		elif y >= len(b):
			c[k:n] = a[x:(n/2)]
			break
		else:
			if a[x] < b[y]:
				c[k] = a[x]
				x = x + 1
			else:
				ind = len(a) + y #Position of the element in b w.r.t merged array
				inv = ind - k
				cnt_inv = cnt_inv + inv
				c[k] = b[y]
				y = y + 1
	

	array[j:j+n] = c
	
	
def main():
  if len(sys.argv) < 2:
    print 'usage: ./merge_sort.py --filename'
    sys.exit(1)
	
  array = []
  filename = sys.argv[1] # This argument has filename argument
  print filename
  with open(filename) as f:
    for line in f:
        data = line.split()
        array.append(int(data[0]))
		
  # TEST data
  #array = [4,2,3,1]
  #array = [6,5,4,3,2,1]
  #array = [1,3,5,2,4,6]
  sorted_array = merge_sort(array)
  print "cnt_inv :", cnt_inv
  print len(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))