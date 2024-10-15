
class undirected_graph:
    def __init__(self,graph):
        self.graph = graph

    def getDegree(self,v):
        degree=0
        for i in self.graph[v]:
            degree+=i
        return degree
    def getNeighbourhood(self,v):
        neighbour=[]
        for i in range(len(self.graph[v])):
            if self.graph[v][i]==1 & i!=v:
                neighbour.append(i)
        return neighbour
    


