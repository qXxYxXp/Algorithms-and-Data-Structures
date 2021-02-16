'''
How to compile and run:
>> python3 quicksort.py
'''
from random import sample, choice
from time import perf_counter

total_p = 0


def randomized_quicksort(S):
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
    randomized_quicksort(R)
    # print(a_i, end=' ')
    randomized_quicksort(T)


def deterministic_quicksort(S):
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
    deterministic_quicksort(R)
    # print(a_i, end=' ')
    deterministic_quicksort(T)


'''
n = 100, 1000, 10000, 100000, 1000000
'''
n = 100
rtotal_time = 0
dtotal_time = 0
for i in range(100):
    S = sample(range(n), k=n)
    # print(S)

    rstart = perf_counter()
    randomized_quicksort(S)
    rend = perf_counter()
    rtotal_time += rend - rstart

    dstart = perf_counter()
    deterministic_quicksort(S)
    dend = perf_counter()
    dtotal_time += dend - dstart
    # print()

print("n = {}".format(n))
print("Randomized quicksort")
print("average time: {}".format(rtotal_time / 100))
print("average time except the time to choose a pivot: {}\n".format((rtotal_time - total_p) / 100))

print("Deterministic quicksort")
print("average time: {}".format(dtotal_time / 100))
