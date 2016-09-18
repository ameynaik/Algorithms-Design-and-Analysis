# Copyright AN. July 2016
#!/usr/bin/python -tt

# Random Contraction Algorithm
# Details on how to implement Adjacency lists to represent sparse graphs is mentioned 
# here : https://algocoding.wordpress.com/2014/08/24/adjacency-list-representation-of-a-graph-python-java/
# implementation details are here : http://stackoverflow.com/questions/10055220/random-contraction-algorithm-for-finding-min-cuts-in-a-graph


import sys
import random
import time
import copy
start_time = time.time()
inv_count = 0
comp_count = 0
dbg_prints = 0

def replace(l, X, Y):
   #print l, X, Y
   for i,v in enumerate(l):
      if v == X:
         l.pop(i)
         l.insert(i, Y)
 

def Randpx(adjList):
	livenodes = []
	for key, value in adjList.items():
		if value:
			livenodes.append(key)
	if dbg_prints:
		print livenodes
	p = random.choice(livenodes)
	x = random.choice(list(set(adjList[p])))
	return (p,x,len(livenodes))
 
def RContractAlgo(adjList):
	'''
	adjList = CutFunc(adjList,5,7)
	adjList = CutFunc(adjList,3,1)
	adjList = CutFunc(adjList,6,8)
	adjList = CutFunc(adjList,4,2)
	adjList = CutFunc(adjList,5,6)
	adjList = CutFunc(adjList,3,4)
	'''
	livenodes = len(adjList.keys())
	while livenodes != 2:
		(p,x,livenodes) = Randpx(adjList)
		if dbg_prints:
			print p,x,livenodes
		if livenodes != 2:
			adjList = CutFunc(adjList,p,x)
		
	for key, value in adjList.items():
		if value:
			mincuts = len(adjList[key])
			return mincuts
	
def CutFunc(adjList,p,x):
	#(p,x) = (5,7)
	#Randpx(adjList) # Function to Choose any node on the graph (let this be denoted by pivot,p) and then Choose any other node on the graph (randomly). (denote this by x)
	# After choosing first vertex, choose another from his adjacency list. Now you are sure that two vertices have the edge between them. Next step is finding the vertex from adjacency list.
  
	adjList[p].extend(adjList[x])
	adjList[x] = []
	#print adjList.items()
  
	for i, j in adjList.items():       # use iteritems in py2k
	#print i,j
		replace(j,x,p)
	#remove self loop
		adjList[i] = list(filter(lambda x: x!= i, j))
		
	if dbg_prints:
		print adjList
  
	return adjList

def main():
  if len(sys.argv) < 2:
    print 'usage: ./RandomContractionAlgorithm.py --filename'
    sys.exit(1)
  
  adjList = {}
  filename = sys.argv[1] # This argument has file name argument
  print filename
  with open(filename) as f:
    for line in f:
        data = map(int,line.split())
        adjList[int(data[0])] = data[1:len(data)]
  
  if dbg_prints:
	print adjList
  
  adjList_orig = copy.deepcopy(adjList)
  
  #print adjList_orig
  
  '''
  mincuts = RContractAlgo(adjList);
  adjList = adjList_orig.copy()
  
  print mincuts,adjList_orig
  '''
  mincuts_lock = 100000
  #mincuts = 1000
  
  for i in range(1000):
	mincuts = RContractAlgo(adjList);
	adjList = copy.deepcopy(adjList_orig)
	#print "loop",i,adjList
	if mincuts < mincuts_lock:
		mincuts_lock = mincuts

  print mincuts_lock
  
  
  #print "This is the input array"
  #print array
  #array = [9,3,4,2,1,7,5,6,8,10]
  #array = [1,2,3,4,5,6]
  #array = [6,5,4,3,2,1]
  #array = [3,4,2]
  #sorted_array = quick_sort(array)
  #print sorted_array
  #print "inv_count : ", inv_count
  #print "comp_count: ", comp_count
  #print len(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))