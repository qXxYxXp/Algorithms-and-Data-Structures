'''
How to compile and run:
>> python3 dfs.py
If you cannot use python3,
>> python2 dfs.py
'''
import copy

time = None


class Vertex:
    def __init__(self, num):
        self.num = num
        self.color = None
        self.discover = None
        self.finish = None


class Edge:
    def __init__(self, fromVertex, toVertex):
        self.fromVertex = fromVertex
        self.toVertex = toVertex


class AdjacencyList:
    def __init__(self, List=None):
        if List is None:
            self.List = {}
        else:
            self.List = List

    def addEdge(self, fromVertex, toVertex):
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        list = copy.copy(self.List)
        list = sorted(list.items(), key=lambda x: x[0])
        for i in list:
            print(i[0], "->", " -> ".join([str(j) for j in i[1]]))


class Graph:
    def __init__(self):
        self.V = dict()
        self.E = set()
        self.Adj = AdjacencyList()

    def addEdge(self, fromVertex, toVertex):
        self.E.add((fromVertex, toVertex))
        self.V.setdefault(fromVertex, Vertex(fromVertex))
        self.V.setdefault(toVertex, Vertex(toVertex))
        self.Adj.addEdge(fromVertex, toVertex)

    def printVertices(self):
        print(self.V)

    def printEdges(self):
        print(self.E)


def DFS_VISIT(G, u):
    global time
    time += 1
    u.discover = time
    u.color = "GRAY"
    for v in G.Adj.List[u.num]:
        if G.V[v].color == "WHITE":
            DFS_VISIT(G, G.V[v])
    u.color = "BLACK"
    time += 1
    u.finish = time


def DFS(G):
    global time
    for i, u in G.V.items():
        u.color = "WHITE"
    time = 0
    for i, u in G.V.items():
        if u.color == "WHITE":
            DFS_VISIT(G, u)


G = Graph()
# make an Adjacecy list
G.addEdge(1, 2)
G.addEdge(1, 4)
G.addEdge(2, 5)
G.addEdge(3, 5)
G.addEdge(3, 6)
G.addEdge(4, 2)
G.addEdge(5, 4)
G.addEdge(6, 6)

DFS(G)

result = copy.copy(G.V)
result = sorted(result.items(), key=lambda x: x[0])

for i, v in result:
    print("Node: {}, discovery time: {}, finishing time: {}".format(i, v.discover, v.finish))

