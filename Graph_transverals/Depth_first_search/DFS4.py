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


    def _DFS(self, visited, current_v):
    	#mark visited node and print it
    	visited[v] = True
    	print(visited[v])

    	#look through adjacent nodes to see if visited
    	#if not visited call node recursivly
    	for i in self.graph[v]:
    		if visited[i] == False:
    			self._DFS(visited, i)


    def DFS(self,v):
    	visited = [False] * len(self.graph)

    	self._DFS(visited, v)