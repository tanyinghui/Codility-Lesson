def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n <= 1:
        return 0
    min_integer = A[0]
    max_diff = A[1] - A[0]
    for i in range(n):
        if A[i] - min_integer > max_diff:
            max_diff = A[i] - min_integer
        if A[i] < min_integer:
            min_integer = A[i]
    return max_diff