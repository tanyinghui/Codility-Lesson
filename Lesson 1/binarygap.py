def solution(N):
    zero = []
    N = bin(N)[2:]
    if (N.count('0') == 0) or (N.count('1') == 1):
        return 0
    else:
        N = N[1:]
        y = N.split('1')
        del y[-1]
        for i in range(len(y)):
            zero.append(len(y[i]))
        zero.sort(reverse = True)
        return zero[0]