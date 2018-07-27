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

	def _DFS(self, v, visited):
 		#mark the current node visited  and print it 
 		visited[v] = True
 		print(v)

 		#for the adjacent verticies to V check if visited and recursivly call if not
 		for i in self.graph[v]:
 			if visited[i] == False:
 				self._DFS(i, visited)




	def DFS(self, v):
    	#create visited array
		visited = [False] * len(self.graph)

    	#call _DFS to handle stack
		self._DFS(v, visited)





graph = Graph()
graph.addEdge(2,0)
graph.addEdge(0,2)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,3)

graph.DFS(2)
