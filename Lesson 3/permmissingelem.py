def solution(A):
    A.sort()
    N = len(A) + 1
    if len(A) == 0:
        return 1
    elif A[-1] != N:
        return N
    for i in range(1, N+1):
        if A[i-1] != i:
            return i