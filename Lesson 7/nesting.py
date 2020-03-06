def solution(S):
    c = 0
    for e in S:
        if e == '(':
            c += 1
        else:
            c -= 1
            if c < 0:
                return 0
    return 1 if c == 0 else 0