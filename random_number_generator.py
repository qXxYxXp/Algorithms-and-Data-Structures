'''
How to compile and run:
>> python3 random_number_generator.py

In python3, there are no limits of muximum value and minimum value, so the part
of checking overflow is different from pseudo code.
'''
from math import ceil

MAX_INT = 2 ** 31 - 1
MIN_INT = -MAX_INT - 1

# counter
cnt1 = [0 for i in range(10)]
cnt2 = [0 for i in range(10)]
cnt3 = [0 for i in range(10)]


def RAND1(n):
    global cnt1

    x = 53402397
    rand_seq = []
    for i in range(n):
        x = 65539 * x + 125654
        if MAX_INT < x:  # check for overflow
            n = ceil((MAX_INT - x) / MIN_INT)
            x += n * MIN_INT
        rand_seq.append(x)
        cnt1[int(((x / MAX_INT) * 10) // 1)] += 1
    return rand_seq


def RAND2(n):
    global cnt2

    x = 1
    A = 48271
    M = 2147483647
    Q = M // A
    R = M % A
    rand_seq = []
    for i in range(n):
        x = A * (x % Q) - R * (x // Q)
        if x < 0:
            x += M
        rand_seq.append(x)
        cnt2[int(((x / MAX_INT) * 10) // 1)] += 1
    return rand_seq


def RAND3(n):
    global cnt3

    x = 1
    next = 0
    A = RAND2(55)
    rand_seq = []
    for i in range(n):
        j = (next + 31) % 55
        x = A[j] - A[next]
        if x < 0:
            x += 2147483647
            x += 1
        A[next] = x
        next = (next + 1) % 55
        rand_seq.append(x)
        cnt3[int(((x / MAX_INT) * 10) // 1)] += 1
    return rand_seq


# n = 10, 1000, or 1000000
n = 1000000

rand1 = RAND1(n)
print(rand1[:5])
for i in range(10):
    print("{:.2f}".format(cnt1[i] / n * 100), end=' ')
print()
# print(sum(cnt1))

rand2 = RAND2(n)
print(rand2[:5])
for i in range(10):
    print("{:.2f}".format(cnt2[i] / n * 100), end=' ')
print()
# print(sum(cnt2))

rand3 = RAND3(n)
print(rand3[:5])
for i in range(10):
    print("{:.2f}".format(cnt3[i] / n * 100), end=' ')
print()
# print(sum(cnt3))
