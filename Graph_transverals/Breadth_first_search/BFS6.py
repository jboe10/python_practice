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

    def BFS(self, start):
    	visited = [False] * len(self.graph())

    	queue = []
    	queue.append(start)
    	visited[start] = True

    	while queue:
    		pop = queue.pop(0)

    		print(pop)

    		for i in self.graph[pop]:
    			if visited[i] == False:
    				visited[i] = True
    				queue.append(i)