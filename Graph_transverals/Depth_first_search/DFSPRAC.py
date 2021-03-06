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

    # A function used by DFS
    def DFSUtil(self,v,visited):
 
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
      
        
 
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self,v):
 
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        
        # Call the recursive helper function to print
        # DFS traversal
        self.DFSUtil(v, visited)
graph = Graph()
graph.addEdge(2,0)
graph.addEdge(0,2)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,3)

graph.DFS(2)