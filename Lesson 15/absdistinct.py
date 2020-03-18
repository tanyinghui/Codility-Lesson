def solution(A):
    # write your code in Python 3.6
    N = [-(e) for e in A if e < 0]
    P = [e for e in A if e >= 0]
    result = set(N + P)
    return len(result)