# 70% O(N*(N+M))

def solution(M, A):
    # write your code in Python 3.6
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p+1, n):
            if len(A[p:q+1]) != len(set(A[p:q+1])):
                break
            result += 1
    return result+n