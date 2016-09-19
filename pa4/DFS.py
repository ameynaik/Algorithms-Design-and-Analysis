# Copyright AN. Aug 2016
#!/usr/bin/python -tt

# This code has Depth First Search routine, Strongly Connected Components routine.

import sys
import random
import time
import copy
from collections import Counter
start_time = time.time()

scc = []
finishingtime = []
visitedGinv = []
visitedGmap = []
value = 0
leader = 0
basicprints = 0

def dfs_iterative(Ginv,s):
    global value
    stack = []
    path_stack = []
    stack.append(s)
        
    while(len(stack)>0):
        #print "amey stack",stack
        v = stack.pop()
        path_stack.append(v)
        #print "path_stack -------> ",path_stack
        if(not visitedGinv[v-1]):
            visitedGinv[v-1] = True
            #print "Processing node ----------------------------",v
            #print visitedGinv
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            #print v,Ginv[v]
            if len(Ginv[v]) == 0:
				value = value + 1
				finishingtime[v-1] = value
				if len(path_stack) > 1:
					path_stack.append(path_stack[-2])
            for w in Ginv[v]:
                #print "v,w = ",v,w,Ginv[w],Ginv[v]
                
                if(not visitedGinv[w-1]):
                    stack_aux.append(w)
                    #print "stack_aux  of ",v,">>>>>>>>>>>> ",stack_aux
                elif(finishingtime[w-1] == 0 and len(Ginv[w]) > 0 and len(Ginv[v]) == 1):              
                    value = value + 1
                    finishingtime[v-1] = value
                    if len(path_stack) > 1:
						path_stack.append(path_stack[-2])
                    #print "I am here ???????????????",value,v,w
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())
                #path_stack.append(v)
                     
    #print "At end of DFS =============================================",finishingtime
    
    #print path_stack
    #return path_stack
    
    while (len(path_stack) > 0):
        v = path_stack.pop()
        #print v
        if finishingtime[v-1] == 0:
			value = value + 1
			finishingtime[v-1] = value
    #print finishingtime		
	
# ------------------------------------------------------------------

def dfs_iterative_leader(Gmap,s):
    global leader
    leader = s
    stack = []
    path_stack = []
    stack.append(s)
        
    while(len(stack)>0):
        #print "amey stack",stack
        v = stack.pop()
        path_stack.append(v)
        #print "path_stack --------------------->",path_stack
        if(not visitedGmap[v-1]):
            visitedGmap[v-1] = True
            #print v
            #print visitedGinv
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            # alternatively: iterate through the adjacency list in reverse order
            # but this is only to get the same output as the recursive dfs
            # otherwise, this would not be necessary
            stack_aux = []
            #print v,Gmap[v]
            if len(Gmap[v]) == 0:
				scc[v-1] = leader
				if len(path_stack) > 1:
					path_stack.append(path_stack[-2])

            for w in Gmap[v]:
                #print "v,w = ",v,w
                if(not visitedGmap[w-1]):
                    stack_aux.append(w)
                elif(scc[w-1] == 0 and len(Gmap[w]) > 0 and len(Gmap[v]) == 1):
                    #print "I am here",value,v,w
                    #value = value + 1
                    scc[v-1] = leader
                    if len(path_stack) > 1:
						path_stack.append(path_stack[-2])
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())
                #path_stack.append(v)
                     
    #print finishingtime
    #print path_stack
    #return path_stack
    
    while (len(path_stack) > 0):
        v = path_stack.pop()
        #print v
        if scc[v-1] == 0:
			scc[v-1] = leader
	#print scc		
	
# ------------------------------------------------------------------

 
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects
	
def main():
	
	if len(sys.argv) < 3:
		print 'usage: ./RandomContractionAlgorithm.py --filename --size'
		sys.exit(1)

	
	filename = sys.argv[1] # This argument has file name argument
	size = int(sys.argv[2])
	Ginv = {}
	G = {}
	
	for i in range(1,size+1):
		if i not in G:
			G[i] = []
			Ginv[i] = []
	
	print filename
	with open(filename) as f:
		for line in f:
			data = map(int,line.split())
			#print data[0],data[1]
			G[data[0]].append(data[1])
			#if data[1] not in Ginv:
			#	Ginv[data[1]] = [];
			Ginv[data[1]].append(data[0])
			#Ginv[int(data[1]-1)].append(int(data[0]-1))
	
	if basicprints:
		print "Ginv",Ginv
		print "G",G
			
	# create the graph in adjacency list representation
	#Ginv = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4] ]
	#Ginv = [ [1,3], [2], [], [2]]
	#Ginv = [ [6], [4], [8], [0], [7], [2,7], [3,8], [1], [5]]
	
	for i in range(0,len(Ginv.keys())): #len(Ginv)):
		visitedGinv.append(False)
		visitedGmap.append(False)
		finishingtime.append(0)
		scc.append(0)
		
	#print visitedGinv
	#print finishingtime
	
	# test our implementation
	for i in xrange(len(Ginv.keys()),0,-1):
		#print i
		
		if visitedGinv[i-1] == False:
			#print "Computing for node",i
			dfs_iterative(Ginv, i)
			#print visitedGinv
			#print finishingtime
	
	if basicprints:
		print finishingtime
	
	# Use G, but map the nodes based on finishing times. 
	# Create mapping dict
	mapft = {}
	for i in range(1,len(finishingtime)+1):
		#print i
		if i not in mapft:
			mapft[i] = finishingtime[i-1];

	Gmap = dict((mapft[key], value) for (key, value) in G.items())
	if basicprints:
		print mapft
		print Gmap
	
	for key in Gmap.keys():
		#print key,Gmap[key]
		Gmap[key] = [mapft[n] for n in Gmap[key]]

	if basicprints:
		print "Gmap",Gmap
	
	scc_list = []	
	# Final DFS loop
	for i in xrange(len(Gmap.keys()),0,-1):
		#print i
		
		if visitedGmap[i-1] == False:
			#print "Computing for node",i
			dfs_iterative_leader(Gmap, i)
			scc_list.append(i)
			#print visitedGmap
	#print scc
	#print scc_list
	a = dict(Counter(scc).most_common(5))
	print a


if __name__ == '__main__':
  main()
  #print ("%s" % (time.time() - start_time))
  
