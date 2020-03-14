def solution(A, B):
    # write your code in Python 3.6
    l = len(A)
    alive = 0
    downstream = []
    for i in range(l):
        if B[i] == 1:
            downstream.append(A[i])
        else:
            while len(downstream) != 0:
                if downstream[-1] > A[i]:
                    break
                else:
                    downstream.pop()
            else:
                alive += 1
    alive += len(downstream)
    return alive