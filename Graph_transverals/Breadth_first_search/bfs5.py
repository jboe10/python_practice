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
    	visited = [False] * (len(self.graph)

    	queue = []

    	#add current node to queue and mark it as visited
    	queue.append(start)
    	visited[start] = True

    	#while qeuue exists
    	while queue:

    		#pop first element and print it
    		pop = queue.pop(0)
    		print(pop)

    		#visit adjacent nodes to pop
    		for i in self.graph[pop]:
    			#if adj isnt visited
    			if visited[i] == False:
    				#append to queue and mark visited
    				queue.append(i)
    				visited[i] = True


