def solution(A):
    A.sort()
    d = dict()
    for value in A:
        if value in d:
            d[value] += 1
        else:
            d[value] = 1
    for key, value in d.items():
        if value%2 != 0:
            return key