'''
How to compile and run:
>> python3 Strassen.py
If you cannot use python3,
>> python2 Strassen.py
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

        # unite C_11, C_12, C_21, C_22
        C = np.vstack((np.hstack((C_11, C_12)), np.hstack((C_21, C_22))))

    return C


def Strassen(A, B):
    n = len(A) // 2

    # Step 1 and Step 2
    S = []
    S.append(B[:n, n:] - B[n:, n:])
    S.append(A[:n, :n] + A[:n, n:])
    S.append(A[n:, :n] + A[n:, n:])
    S.append(B[n:, :n] - B[:n, :n])
    S.append(A[:n, :n] + A[n:, n:])
    S.append(B[:n, :n] + B[n:, n:])
    S.append(A[:n, n:] - A[n:, n:])
    S.append(B[n:, :n] + B[n:, n:])
    S.append(A[:n, :n] - A[n:, :n])
    S.append(B[:n, :n] + B[:n, n:])

    # Step 3
    P = []
    P.append(MAT_MULT(A[:n, :n], S[0]))
    P.append(MAT_MULT(S[1], B[n:, n:]))
    P.append(MAT_MULT(S[2], B[:n, :n]))
    P.append(MAT_MULT(A[n:, n:], S[3]))
    P.append(MAT_MULT(S[4], S[5]))
    P.append(MAT_MULT(S[6], S[7]))
    P.append(MAT_MULT(S[8], S[9]))

    # Step 4
    C_11 = P[4] + P[3] - P[1] + P[5]
    C_12 = P[0] + P[1]
    C_21 = P[2] + P[3]
    C_22 = P[0] + P[4] - P[2] - P[6]

    C = np.vstack((np.hstack((C_11, C_12)), np.hstack((C_21, C_22))))

    return C


'''
n = 32, 64, 128, 256, 512, or 1024
'''
n = 32
A = np.random.randint(0, 9, (n, n))
B = np.random.randint(0, 9, (n, n))

start = time.time()  # if python3, time.perf_counter()
C = Strassen(A, B)
end = time.time()  # if python3, time.perf_counter()

# np.set_printoptions(linewidth=10*n*n, threshold=n*n)
# print(A, '\n')
# print(B, '\n')
# print(C)
print("Strassen: n = {}\nexecution time: {}".format(n, end - start))
