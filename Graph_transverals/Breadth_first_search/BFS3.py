# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
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

	def BFS(self, v):
		visited = [False] * len(self.graph)

		queue = []

		queue.append(v)
		visited[v] = True



		while queue:
			s = queue.pop(0)
			print(s, end=" ")

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


graph = Graph()
graph.addEdge(2,0)
graph.addEdge(0,2)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,3)

print(graph)
graph.BFS(0)