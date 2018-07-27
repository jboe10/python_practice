from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)


    def BFS(self,start):
    	#make visited
    	#make queue
    	visited = [False] * (len(self.graph))
    	qeueu = []


    	#append start to queue, mark as visited
    	qeueu.append(start)
    	visited[start] = True

    	while queue:
    		#pop queue and print it
    		start = queue.pop(0)
    		print(start)

    		#look through adjacent of popped
    		#if not visited append to queue and mark as visited
    		for i in self.graph[start]
    			if visited[i] == False:
    				queue.append(i)
    				visisted[i] = True

