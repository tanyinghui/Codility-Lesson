def solution(X, Y, D):
    Y -= X
    n = Y//D
    k = Y%D
    if k > 0:
        return n+1
    else: 
        return n