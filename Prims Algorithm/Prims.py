INF = 9999999

class Graph:
    def __init__(self, nodes, edges):
        self.edges = edges
        self.nodes = nodes
        self.numVertices = len(edges)
        self.MST = []
    
    def printSolution(self):
        totalWeight = 0
        for s, d, w in self.MST:
            print("({}, {})".format(s,d))
            totalWeight += w
        print("Total weight of MST is {}".format(totalWeight))
    
    def primsAlgo(self):
        visited = [0]*self.numVertices
        edgeNum=0
        visited[0]=True
        while edgeNum<self.numVertices-1:
            min = INF
            for i in range(self.numVertices):
                if visited[i]:
                    for j in range(self.numVertices):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edgeNum += 1
        self.printSolution()



V = ["A","B","C","D"]

E = [[0, 1, 4, 3],
    [1, 0, 0, 2],
    [4, 0, 0, 5],
    [3, 2, 5, 0]]


g = Graph(V, E)
g.primsAlgo()
