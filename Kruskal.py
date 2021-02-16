'''
How to compile and run:
>> python3 Kruskal.py
If you cannot use python3,
>> python2 Kruskal.py
'''


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.root = [i for i in range(size + 1)]
        self.weight = [0 for i in range(size + 1)]

    def FIND_SET(self, u):
        if u != self.root[u]:
            self.root[u] = self.FIND_SET(self.root[u])

        return self.root[u]

    def UNION(self, u, v):
        if u == v:
            return

        root_u = self.FIND_SET(u)
        root_v = self.FIND_SET(v)
        weight_u = self.weight[root_u]
        weight_v = self.weight[root_v]
        if weight_u >= weight_v:
            self.root[root_v] = root_u
            if weight_u == weight_v:
                self.weight[root_u] += 1
        else:
            self.root[root_u] = root_v


class Edge:
    def __init__(self, fromVertex, toVertex):
        self.fromVertex = fromVertex
        self.toVertex = toVertex


class Graph:
    def __init__(self):
        self.V = set()
        self.E = []

    def addEdge(self, fromVertex, toVertex, cost):
        self.V.add(fromVertex)
        self.V.add(toVertex)
        self.E.append((fromVertex, toVertex, cost))


def MST_KRUSKAL(G):
    MST = set()
    MST_cost = 0

    U = UnionFind(len(G.V))

    G.E = sorted(G.E, key=lambda edge: edge[2])

    for u, v, cost in G.E:
        if U.FIND_SET(u) != U.FIND_SET(v):
            MST_cost += cost
            MST.add((u, v))
            U.UNION(u, v)

    return (MST, MST_cost)


G = Graph()
G.addEdge(1, 2, 20)
G.addEdge(1, 7, 1)
G.addEdge(1, 6, 23)
G.addEdge(2, 3, 15)
G.addEdge(2, 7, 4)
G.addEdge(3, 4, 3)
G.addEdge(3, 7, 9)
G.addEdge(4, 5, 17)
G.addEdge(4, 7, 16)
G.addEdge(5, 6, 28)
G.addEdge(5, 7, 25)
G.addEdge(6, 7, 36)

edges, total_weight = MST_KRUSKAL(G)
edges = sorted(edges)
print("edges: {}".format(edges))
print("sum of weight: {}".format(total_weight))
