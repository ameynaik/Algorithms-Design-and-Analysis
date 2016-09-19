# Copyright AN. Aug 2016
#!/usr/bin/python -tt

# Dijkstra's Algorithm

import sys
import random
import time
import copy
from collections import Counter
start_time = time.time()


def main():
	
	if len(sys.argv) < 3:
		print 'usage: python DijkstraAlgo.py --filename --size'
		sys.exit(1)

	
	filename = sys.argv[1] # This argument has file name argument
	size = int(sys.argv[2])
	G = {}
	Avs = {}
	X = [] # Visited nodes.
	#size = 6 #4
	
	for i in range(1,size+1):
		if i not in G:
			G[i] = []
			Avs[i] = 0
				
	print filename
	with open(filename) as f:
		for line in f:
			data = line.split()#map(int,line.split())
			for i in range(1,len(data)):
				tuple = data[i].split(',')
				x = (int(tuple[0]),int(tuple[1]))
				G[int(data[0])].append(x)

	#print G

	s = 1; t = 7; # start and end nodes.
	X.append(s)
	#print Avs
	node = s;
	while len(X) != size:
		min = 1000000;
		for node in X:
			for i in range(0,len(G[node])):
				if G[node][i][0] not in X:
					#print "processing node,i = ",node,G[node][i][0]
					if (G[node][i][1] + Avs[node] < min):
						min = G[node][i][1] + Avs[node]; w = G[node][i][0]
					#print min,w
			
		X.append(w)
		Avs[w] = min
		node = w
	
	print Avs[7],Avs[37],Avs[59],Avs[82],Avs[99],Avs[115],Avs[133],Avs[165],Avs[188],Avs[197]
	

if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))
  
