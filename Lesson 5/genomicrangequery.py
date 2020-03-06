def checking(S):
    if 'A' in S:
        return 1
    elif 'C' in S:
        return 2
    elif 'G' in S:
        return 3
    elif 'T' in S:
        return 4

def solution(S, P, Q):
    res = [0]*len(P)
    for i in range(len(res)):
        res[i] = checking(S[P[i]:Q[i]+1])
    return res