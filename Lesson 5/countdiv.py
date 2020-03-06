def solution(A, B, K):
    return ((B-A)//K)+1 if A%K == 0 else (B-(A-A%K))//K