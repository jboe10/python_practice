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

    def BFS(self, s):
    	#mark all as univisited
        visited = [False] * (len(self.graph))

    	#create a queue for BFS
        queue = []
    
    	#mark the source node as visited and enqueue it 
        visited[s] = True
        queue.append(s)

    	
    		#dequeue a vertex from queue and print it
        while queue:
            s = queue.pop(0)
            print(s, end = " ")

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

graph.BFS(2)