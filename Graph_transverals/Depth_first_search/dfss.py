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

   	def DFS(self, start):
   		visited = [False] * (len(self.graph))
   		self._DFS(start, visited)

   	def _DFS(self, visited, start):
   		visited[start] = True
   		print(start)

   		for i in self.graph[start]:
   			if visited[i] == False:
   				self._DFS(visited, i)