from random import sample, choice
from time import perf_counter

total_p = 0


def quicksort(S):
    global total_p
    if len(S) == 0:
        return
    R = []
    T = []
    ps = perf_counter()
    a_i = choice(S)
    pe = perf_counter()
    total_p += pe - ps
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
print("Randomized quicksort")
print("n = {}".format(n))
print("average time: {}".format(total_time / 100))
print("average time except the time to choose a pivot: {}".format((total_time - total_p) / 100))
