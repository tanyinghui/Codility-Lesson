def solution(A):
    # write your code in Python 3.6
    n = len(A)
    c = n//2
    size = 0
    for i in range(n):
        if (size == 0):
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
    s = A.count(value)
    leader = value if s > n//2 else None
    if leader is None:
        return 0
    elif s == n:
        return n-1
    equi = a = 0
    for i in range(n):
        if A[i] == leader:
            a += 1
        if a > (i+1)//2 and (s-a) > (n-i-1)//2:
            equi += 1
    return equi