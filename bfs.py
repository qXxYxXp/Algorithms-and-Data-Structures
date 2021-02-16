'''
How to compile and run:
>> python3 bfs.py
If you cannot use python3,
>> python2 bfs.py
'''
import copy
from collections import deque


class Vertex:
    def __init__(self, num):
        self.num = num
        self.color = None
        self.dist = None
        self.parent = None


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


def BFS(G, s):
    for i, u in G.V.items():
        u.color = "WHITE"
        u.dist = 0
        u.parent = None
    s.color = "GRAY"
    Q = deque()
    Q.append(s)  # Q.push(s)
    while len(Q) > 0:
        u = Q.popleft()
        for v in G.Adj.List[u.num]:
            if G.V[v].color == "WHITE":
                G.V[v].color = "GRAY"
                G.V[v].dist = u.dist + 1
                G.V[v].parent = u
                Q.append(G.V[v])
        u.color = "BLACK"


G = Graph()
# make an Adjacecy List
G.addEdge(0, 8)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(1, 7)
G.addEdge(1, 9)
G.addEdge(2, 1)
G.addEdge(2, 4)
G.addEdge(2, 8)
G.addEdge(3, 1)
G.addEdge(3, 4)
G.addEdge(3, 5)
G.addEdge(4, 2)
G.addEdge(4, 3)
G.addEdge(5, 3)
G.addEdge(5, 6)
G.addEdge(6, 5)
G.addEdge(6, 7)
G.addEdge(7, 1)
G.addEdge(7, 6)
G.addEdge(8, 0)
G.addEdge(8, 2)
G.addEdge(8, 9)
G.addEdge(9, 1)
G.addEdge(9, 8)


BFS(G, G.V[1])

result = copy.copy(G.V)
result = sorted(result.items(), key=lambda x: x[0])

for i, v in result:
    print("Node: {}, distance: {}".format(i, v.dist))
