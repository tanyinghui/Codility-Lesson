def solution(A):
    # write your code in Python 3.6
    data = {}
    l = len(A)
    for e in A:
        if e not in data.keys():
            data[e] = 1
        else:
            data[e] += 1
            if data[e] > l//2:
                return A.index(e)
    return 0 if l == 1 else -1