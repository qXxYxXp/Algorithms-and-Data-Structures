'''
How to compile and run:
>> python3 n_queens_problem.py
If you cannot use python3,
>> python2 n_queens_problem.py
'''
from __future__ import print_function


n = 8
positionInRow = [True for i in range(n)]
column = [True for i in range(n)]
leftDiag = [True for i in range(2 * n)]
rightDiag = [True for i in range(2 * n)]
count = 0


def PrintBoard():
    global n, positionInRow

    for i in range(n):
        for j in range(n):
            if positionInRow[i] == j:
                print('Q', end='')
            else:
                print('-', end='')
        print()


def PutQueen(row):
    global n, positionInRow, column, leftDiag, rightDiag, count

    for col in range(n):
        if column[col] and leftDiag[row + col] and rightDiag[row - col + n - 1]:
            positionInRow[row] = col
            column[col] = False
            leftDiag[row + col] = False
            rightDiag[row - col + n - 1] = False
            if row < n - 1:
                PutQueen(row + 1)
            else:
                print("solution found")
                count += 1
                PrintBoard()
            column[col] = True
            leftDiag[row + col] = True
            rightDiag[row - col + n - 1] = True


PutQueen(0)

print("The number of solutions: {}".format(count))
