def solution(A):
    return min(set(range(1 ,len(A) + 2)) - set(A))