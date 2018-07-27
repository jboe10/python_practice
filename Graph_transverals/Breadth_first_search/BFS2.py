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
		#mark all as univisited
		visited = [False] * (len(self.graph))

    	#create a queue for BFS
		queue = []
    	

    	#mark the source node as visited and enqueue it 
		visited[v]
		qeueu.append(v)

		while queue:
    		#dequeue a vertex from queue and print it
			vertex = qeueu.pop(0)
			print(vertex)

    		#get all adjacent verticies of the dequeued vertex s
    		#if an adjacent has not been visited, then mark it visited and enqueue it
		for i in self.graph[v]:
			if visited[i] == False:
				visited[i] = True
				queue.append(i)
    		