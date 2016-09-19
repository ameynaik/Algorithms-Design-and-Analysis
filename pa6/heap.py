# Copyright AN. December 2015
#!/usr/bin/python -tt
# Heap Data Structure
# Source : https://youtu.be/v1YUApMYXO4

import math
import random

# 1. AddElement function.

def AddElement(heap,ele): # Add element to the heap and return the heap
	heap.append(ele) # append ele at the end of the heap.
	i = len(heap) - 1
	if len(heap) != 1:
		while i != 0:
			if heap[i] > heap[parentnode(i)]:
				heap[parentnode(i)],heap[i] = heap[i],heap[parentnode(i)]
			i = ((i -1) >> 1) 
	return heap
		
# 2. RemoveElement function

def RmElement(heap):
	heap[0],heap[len(heap)-1] = heap[len(heap)-1],heap[0]
	heap = heap[0:len(heap)-1]
	parent_indx = 0
	heap_complete = 0;
	
	while heap_complete != 1:
	
		[c1,c2] = childnodes(parent_indx)
		
		if (c1 >= len(heap)): #or c2 >= len(heap)):
			#which means we are at the end
			heap_complete = 1
			
		elif (c2  >= len(heap)):
			if heap[c1] > heap[parent_indx]:
				heap[c1],heap[parent_indx] = heap[parent_indx],heap[c1]
			heap_complete = 1
			
		else:
			if heap[c1] > heap[c2]:
				max_child_idx = c1
			else:
				max_child_idx = c2
		
			if heap[parent_indx] < heap[max_child_idx]:
				heap[parent_indx],heap[max_child_idx] = heap[max_child_idx],heap[parent_indx]
				parent_indx = max_child_idx
			else: 
				heap_complete = 1
	
	return heap
			


def parentnode(idx): # returns index of Parent of the heap element
	pidx = ((idx - 1)>>1)
	return pidx	

def childnodes(idx): # returns indices of child node.
	cidx1 = (idx << 1) + 1 
	cidx2 = (idx << 1) + 2 
	return [cidx1,cidx2]
	
def displayheap(heap):
	i = len(heap)
	#while i != 0:
	print '\t\t',heap[0]
	print '\t',heap[1],'\t\t',heap[2]
	print '      ',heap[3],heap[4],'\t\t',heap[5],heap[6]
	print heap[7],heap[8],'\t  ',heap[9],heap[10],'\t',heap[11],heap[12]
		

def main():

  #arr = [67,78,62,64,69,61,0,58,41,5,24,45,27,34,81]
  #arr = [1,2,3,4,5,6]
  arr = [-1,-2]
  heap = []
  #random.shuffle(arr)
  #arr = [69,64,0,24,58,27,67,34,5,41,62,78,45,61,81]
  #arr = [24,0,5]
  print arr
  for item in range(len(arr)):
	AddElement(heap,arr[item])
  
  print heap
  print 'Its complete',heap
  #displayheap(heap)
  heap = RmElement(heap)
  print 'Its complete',heap
  #displayheap(heap)
  #heap = RmElement(heap)
  print 'Its complete',heap
  #displayheap(heap)


if __name__ == '__main__':
  main()

