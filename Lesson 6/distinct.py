def solution(A):
    n = len(A)
    if n < 1:
        return 0
    d = 1
    A.sort()
    for i in range(n-1):
        if A[i] != A[i+1]:
            d += 1
    return d