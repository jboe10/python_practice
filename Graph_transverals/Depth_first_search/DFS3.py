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

	def _DFS(self, visited, v):
		visited[v] = True
		print(visited[v])

		for i in self.graph:
			if(visited[i] == False):
				self._DFS(visited, i)


	def DFS(self, v):

		visited = [False] * len(self.graph)

		self._DFS(visited, v)