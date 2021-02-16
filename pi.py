from random import random


def PI(n):
    inCircle = 0
    for i in range(n):
        x = random()
        y = random()
        d = (x - 0.5) ** 2 + (y - 0.5) ** 2
        if d < 0.25:
            inCircle += 1
    return 4 * inCircle / n


'''
n = 1, 10, 100, 1000, 10000, or 100000
'''
n = 100000
print("n = {}".format(n))
for i in range(10):
    print("{}: {}".format(i + 1, PI(n)))
