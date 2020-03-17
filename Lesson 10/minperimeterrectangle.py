def solution(N):
    # write your code in Python 3.6
    i = 1
    P = 2 * (N+N)
    while (i*i) <= N:
        if (N%i == 0):
            P = min(P,2*(i+(N//i)))
        i += 1
    return P