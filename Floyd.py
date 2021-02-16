def FLOYD(W):
    D = W
    for k in W:
        for i in W:
            for j in W:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    # return D  # need not to use this


f_inf = float("inf")
W = {'a': {'a': 0,     'b': 48,    'c': f_inf, 'd': 8,     'e': 20,    'f': f_inf, 'g': 20,    'h': f_inf},
     'b': {'a': f_inf, 'b': 0,     'c': 24,    'd': f_inf, 'e': 9,     'f': f_inf, 'g': 76,    'h': 29   },
     'c': {'a': 97,    'b': f_inf, 'c': 0,     'd': f_inf, 'e': f_inf, 'f': f_inf, 'g': 18,    'h': 1    },
     'd': {'a': f_inf, 'b': 52,    'c': 34,    'd': 0,     'e': 29,    'f': f_inf, 'g': f_inf, 'h': f_inf},
     'e': {'a': f_inf, 'b': f_inf, 'c': f_inf, 'd': f_inf, 'e': 0,     'f': 10,    'g': f_inf, 'h': f_inf},
     'f': {'a': f_inf, 'b': 10,    'c': 85,    'd': 43,    'e': f_inf, 'f': 0,     'g': 41,    'h': 29   },
     'g': {'a': f_inf, 'b': f_inf, 'c': f_inf, 'd': 76,    'e': 38,    'f': f_inf, 'g': 0,     'h': f_inf},
     'h': {'a': 28,    'b': 42,    'c': f_inf, 'd': 77,    'e': 21,    'f': f_inf, 'g': 11,    'h': 0    }}

FLOYD(W)

for i, j in W.items():
    print("{}:{{".format(i), end='')
    for k, l in j.items():
        print("{}:{:>3}".format(k, l), end=', ' if k != 'h' else '')
    print("}")
