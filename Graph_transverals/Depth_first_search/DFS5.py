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

    def DFS_P(self,starting_edge,visited):
    	
    	visited[starting_edge] = True
    	print(starting_edge)

    	for i in self.graph(starting_edge):
    		if visited[i] == False:
    			self.DFS_P(i,visited)


    def DFS(self, starting_edge):

    	visisted = [False] * (len(self.graph))
    	
    	self.DFS_p(starting_edge, visited)