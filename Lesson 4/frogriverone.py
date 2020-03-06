def solution(X, A):
    n = [-1] * X
    for idx, e in enumerate(A):
        if n[e-1] == -1:
            n[e-1] = idx
        else:
            continue
    return max(n) if -1 not in n else -1