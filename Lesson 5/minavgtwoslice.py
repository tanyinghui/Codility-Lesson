def findavg(A):
    return sum(A)/len(A)

def solution(A):
    n = len(A)
    pos = 0
    current = findavg(A)
    for i in range(1,n-1):
        avg2 = findavg(A[i:i+2])
        if avg2 < current:
            current = avg2
            pos = i
    for i in range(n-2):
        avg3 = findavg(A[i:i+3])
        if avg3 < current:
            current = avg3
            pos = i
    return pos