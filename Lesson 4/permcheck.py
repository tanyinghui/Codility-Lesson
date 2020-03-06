def solution(A):
    B = []
    for i in range(1,len(A)+1):
        B.append(i)
    return int(set(B) == set(A))