'''
How to compile and run:
>> python3 matrix_chain_multiplication.py
If you cannot use python3,
>> python2 matrix_chain_multiplication.py
'''


def MATRIX_CHAIN_ORDER(r):
    n = len(r) - 1
    m = [[None for i in range(n + 1)] for j in range(n + 1)]
    s = [[None for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, (n - l + 1) + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, (j - 1) + 1):
                q = m[i][k] + m[k + 1][j] + r[i - 1] * r[k] * r[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return (m, s)


def PRINT_OPTIMAL_PARENS(s, i, j):
    if i == j:
        print("M{}".format(i), end='')
    else:
        print("(", end='')
        PRINT_OPTIMAL_PARENS(s, i, s[i][j])
        PRINT_OPTIMAL_PARENS(s, s[i][j] + 1, j)
        print(")", end='')


def PRINT_MATRICES(m, s):
    print("matrix m:\n   ", end='')
    for i in range(2, len(m[1])):
        print("     M{}".format(i), end='')
    print()
    for i in range(1, len(m) - 1):
        print("M{} ".format(i), end='')
        for j in range(2, len(m[i])):
            if (m[i][j] is None) or (m[i][j] == 0):
                print("       ", end='')
            else:
                print("{:>7}".format(m[i][j]), end='')
        print()
    print("----------------------------------------")

    print("matrix s:\n   ", end='')
    for i in range(2, len(s[1])):
        print(" M{}".format(i), end='')
    print()
    for i in range(1, len(s) - 1):
        print("M{} ".format(i), end='')
        for j in range(2, len(s)):
            if s[i][j] is None:
                print("   ", end='')
            else:
                print("{:>3}".format(s[i][j]), end='')
        print()
    print("----------------------------------------")


'''
Problem 1: [5, 10, 3, 12, 5, 50, 6]
Problem 2:
a): [30, 35, 15, 5, 10, 20, 25]
b): [10, 20, 10, 15, 20, 10]
c): [100, 10, 100, 1, 1000, 100]
'''
r = [5, 10, 3, 12, 5, 50, 6]

m, s = MATRIX_CHAIN_ORDER(r)

PRINT_MATRICES(m, s)
PRINT_OPTIMAL_PARENS(s, 1, len(r) - 1)
print("\nMinimum cost: {}".format(m[1][len(r) - 1]))
