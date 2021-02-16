'''
How to compile and run:
>> python3 merge_sort.py
If you cannot use python3
>> python2 merge_sort.py
'''


def merge(A, B):
    result = []
    while len(A) > 0 or len(B) > 0:
        if len(A) > 0 and len(B) > 0:
            if A[0] <= B[0]:
                result.append(A.pop(0))
            else:
                result.append(B.pop(0))
        elif len(A) > 0:
            result.append(A.pop(0))
        elif len(B) > 0:
            result.append(B.pop(0))
    return result


def merge_sort(A):
    if len(A) > 1:
        middle = len(A) // 2
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:])
        return merge(left, right)
    else:
        return A


A = [6, 5, 3, 1, 8, 7, 2, 4]
result = merge_sort(A)
print(result)
