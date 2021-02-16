'''
How to compile and run:
>> python3 recursive_matrix_production.py
If you cannot use python3,
>> python2 recursice_matrix_production.py
'''
import numpy as np
import time


def MAT_MULT(A, B):
    n = len(A)
    if n == 1:
        C = A * B
    else:
        n //= 2
        C_11 = MAT_MULT(A[:n, :n], B[:n, :n]) + MAT_MULT(A[:n, n:], B[n:, :n])
        C_12 = MAT_MULT(A[:n, :n], B[:n, n:]) + MAT_MULT(A[:n, n:], B[n:, n:])
        C_21 = MAT_MULT(A[n:, :n], B[:n, :n]) + MAT_MULT(A[n:, n:], B[n:, :n])
        C_22 = MAT_MULT(A[n:, :n], B[:n, n:]) + MAT_MULT(A[n:, n:], B[n:, n:])

        # unite C_11, C_12, C_21, and C_22
        C = np.vstack((np.hstack((C_11, C_12)), np.hstack((C_21, C_22))))

    return C


'''
n = 32, 64, 128, 256, 512, or 1024
'''
n = 32
A = np.random.randint(0, 9, (n, n))
B = np.random.randint(0, 9, (n, n))

start = time.time()  # if python3, time.perf_counter()
C = MAT_MULT(A, B)
end = time.time()  # if python3, time.perf_counter()

# np.set_printoptions(linewidth=10*n*n, threshold=n*n)
# print(A, '\n')
# print(B, '\n')
# print(C)
print("Recursive: n = {}\nexecution time: {}".format(n, end - start))
