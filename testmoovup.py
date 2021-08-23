from collections import defaultdict
from operator import itemgetter

class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)
    def addEdge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def printAllPathsUtil(self, u, d, visited, path):
            # Mark the current node as visited and store in path
            visited[u]= True
            path.append(u)

            # If current vertex is same as destination, then print
            # current path[]
            if u == d:
            # Map numbers to alphabets to reflect real node names
                pathslib.append([chr(65+number) for number in path])
                print ([chr(65+number) for number in path])
            else:
                # If current vertex is not destination
                # Recur for all the vertices adjacent to this vertex
                for i in self.graph[u]:
                    if visited[i]== False:
                        self.printAllPathsUtil(i, d, visited, path)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()
            visited[u]= False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited =[False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
    def printShortestPath(self):
        #Number of nodes reached for each path
        lengths = [len(x) for x in pathslib]
        #Minnimun Number of nodes
        v = min (lengths)
        indices = [i for i, x in enumerate(lengths) if x == v]
        for i in indices:
            print(pathslib[i])
        print('Minimum number of hops is: %d' %(v - 1))


# Driver program to test methods of graph class
if __name__ == '__main__':
    path = " "
    pathslib = [];
    listof = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    # Create a graph given in the diagram
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge( 0, 7)
    g.addEdge( 0, 3)
    g.addEdge( 1, 3)
    g.addEdge( 1, 2)
    g.addEdge( 2, 3)
    g.addEdge( 2, 5)
    g.addEdge( 3, 4)
    g.addEdge( 4, 5)
    g.addEdge( 4, 7)
    g.addEdge(5, 6)
    g.addEdge( 6, 7)
    #change start and end to desired path
    start = "A"; end = "H"
    s = listof.index(start); d = listof.index(end)
    print ("Following are all different paths from % d to % d :" %(s, d))
    g.printAllPaths(s, d)
    print("Shortest path is:")
    g.printShortestPath()
