def solution(A):
    # write your code in Python 3.6
    l = len(A)
    size = 0
    for i in range(l):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
    candidate = value if size > 0 else -1
    leader = -1
    count = 0
    for j in range(l):
        if A[j] == candidate:
            count += 1
    return A.index(candidate) if count > l//2 else leader