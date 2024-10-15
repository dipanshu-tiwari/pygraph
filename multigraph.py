class directed_graph:
    def __init__(self, graph):
        self.graph = graph
        self.noVertices = len(self.graph)
    def getinDegree(self, n):
        degree = 0
        for i in range(self.noVertices):
            degree += self.graph[i][n]
        return degree
    def getoutDegree(self, n):
        degree = 0
        for i in self.graph[n]:
            degree += i
        return degree
    def getDegree(self, n):
        return self.getinDegree(n) + self.getoutDegree(n)