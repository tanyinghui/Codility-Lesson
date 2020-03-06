def solution(A):
    A.sort(reverse=True)
    pos = A[0]*A[1]*A[2]
    neg = A[-1]*A[-2]*A[0]
    return neg if neg > pos else pos