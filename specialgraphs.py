from undirected_graph.py import undirected_graph

class complete_graph(undirected_graph):
    def __init__(self, n):
        self.graph = []
        for i in range(n):
            tmp = []
            for j in range(n):
                if (i==j):
                    tmp.append(0)
                else:
                    tmp.append(1)
            self.graph.append(tmp)
        self.noVertices = n

class cycle_graph(undirected_graph):
    def __init__(self, n):
        self.graph = []
        for i in range(n-1):
            tmp = []
            for j in range(n):
                if (i + 1 == j):
                    tmp.append(1)
                else:
                    tmp.append(0)
            self.graph.append(tmp)
        tmp = [1]
        for i in range(n-1):
            tmp.append(0)
        self.graph.append(tmp)
        self.noVertices = n

class wheel_graph(undirected_graph):
    def __init__(self, n):
        self.graph = []
        for i in range(n-1):
            tmp = []
            for j in range(n):
                if (i + 1 == j):
                    tmp.append(1)
                else:
                    tmp.append(0)
            tmp.append(1)
            self.graph.append(tmp)
        tmp = [1]
        for i in range(n-1):
            tmp.append(0)
        self.graph.append(tmp)
        tmp = []
        for i in range(n-1):
            tmp.append(1)
        tmp.append(0)
        self.graph.append(tmp)
        self.noVertices = n