def solution(A):
    n = len(A)
    west = 0
    pair = 0
    for i in range(n-1,-1,-1):
        if A[i] == 0:
            pair += west
            if pair > 1000000000:
                return -1
        else:
            west += 1
    return pair