class Graph:
    def __init__(self, W):
        self.V = []
        for i in W:
            self.V.append(i)

        self.E = []
        for i, v in W.items():
            for j, w in v.items():
                if W[i][j]:
                    self.E.append((i, j))

        self.T = {}


def WARSHALL(G):
    # n = len(G.V) need not to use this
    for i in G.V:
        G.T[i] = {}
        for j in G.V:
            if i == j or (i, j) in G.E:
                G.T[i][j] = 1
            else:
                G.T[i][j] = 0
    for k in G.V:
        for i in G.V:
            for j in G.V:
                G.T[i][j] = G.T[i][j] or (G.T[i][k] and G.T[k][j])
    return G.T


W = {'a': {'a': 0, 'b': 1, 'c': 0, 'd': 0, 'e': 1, 'f': 1, 'g': 0, 'h': 1},
     'b': {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 0, 'f': 0, 'g': 1, 'h': 0},
     'c': {'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 0, 'f': 0, 'g': 1, 'h': 0},
     'd': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 1, 'g': 0, 'h': 0},
     'e': {'a': 0, 'b': 0, 'c': 1, 'd': 0, 'e': 0, 'f': 1, 'g': 0, 'h': 0},
     'f': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 1, 'h': 0},
     'g': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 1},
     'h': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 1, 'g': 1, 'h': 0}}
G = Graph(W)

T = WARSHALL(G)

for i, j in T.items():
    print("{}:{{".format(i), end='')
    for k, l in j.items():
        print("{}:{}".format(k, l), end=', ' if k != 'h' else '')
    print("}")
