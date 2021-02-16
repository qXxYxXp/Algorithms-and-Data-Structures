'''
How to compile and run:
>> python3 heap_bottom_up.py
If you cannot use python3,
>> python2 heap_bottom_up.py
'''

def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def MaxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swap
        MaxHeapify(A, largest)


def HeapBottomUp(A):
    for i in range((len(A) - 1) // 2, 0, -1):
        MaxHeapify(A, i)


A = [-1, 6, 13, 9, 5, 12, 8, 7, 4, 0]  # 1-indexed
HeapBottomUp(A)
print(A[1:])
