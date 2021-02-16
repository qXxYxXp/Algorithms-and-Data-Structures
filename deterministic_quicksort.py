from random import sample
from time import perf_counter


def quicksort(S):
    if len(S) == 0:
        return
    R = []
    T = []
    a_i = S[0]
    for a in S:
        if a < a_i:
            R.append(a)
        if a > a_i:
            T.append(a)
    quicksort(R)
    # print(a_i, end=' ')
    quicksort(T)


'''
n = 100, 1000, 10000, 100000, 1000000
'''
n = 1000000
total_time = 0
for i in range(100):
    S = sample(range(n), k=n)
    # print(S)
    start = perf_counter()
    quicksort(S)
    end = perf_counter()
    total_time += end - start
    # print()
print("Deterministic quicksort")
print("n = {}".format(n))
print("average time: {}".format(total_time / 100))
