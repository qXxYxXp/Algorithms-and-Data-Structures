'''
How to compile and run:
>> python3 Dijkstra.py
If you cannot use python3,
>> python2 Dijkstra.py
'''
import heapq


class Graph:
    def __init__(self):
        self.V = {}
        self.Adj = {}
        self.w = {}

    def makew(self):
        for k, v in self.Adj.items():
            self.w[k] = {}
            for i, d in v:
                self.w[k][i] = d


def MIN_PRIORITY_QUEUE(V):
    Q = []
    for k, v in V.items():
        heapq.heappush(Q, (v[1], v[0]))
    return Q


def INIT_SS(G, s):
    for i in G.Adj:
        G.V[i] = [i, 10000, "NIL"]  # [name, cost, predecessor]
    G.V[s][1] = 0


def RELAX(G, Q, u, v, w):
    if G.V[v][1] > G.V[u][1] + w[u][v]:
        G.V[v][1] = G.V[u][1] + w[u][v]
        G.V[v][2] = G.V[u][0]
        heapq.heappush(Q, (G.V[v][1], G.V[v][0]))


def DIJKSTRA(G, s, w):
    INIT_SS(G, s)
    Q = MIN_PRIORITY_QUEUE(G.V)
    while Q:
        cost, u = heapq.heappop(Q)
        for v in G.Adj[u]:
            RELAX(G, Q, u, v[0], w)


def printShortestPath(G, v):
    if G.V[v][2] == "NIL":
        print(v, end='')
        return
    printShortestPath(G, G.V[v][2])
    print(" -> {}".format(v), end='')


G = Graph()
G.Adj = {'A': [['B', 8], ['C', 2], ['D', 4]],
         'B': [['A', 8], ['C', 7], ['E', 2]],
         'C': [['A', 2], ['B', 7], ['D', 1], ['E', 3], ['F', 9]],
         'D': [['A', 4], ['C', 1], ['F', 5]],
         'E': [['B', 2], ['C', 3]],
         'F': [['C', 9], ['D', 5]]}
G.makew()
DIJKSTRA(G, 'A', G.w)
print("The obtained shortest path from start to each vertex and cost")
for i in G.V:
    print("{}: ".format(i), end='')
    printShortestPath(G, i)
    print(" (cost: {})".format(G.V[i][1]))
