def solution(A, K):
    l = len(A)
    if l == 0 or K == 0:
        return A
    B = [0]*l
    for i in range(0, l):
        j = ((i+K)%l)
        B[j] = A[i]
    return B