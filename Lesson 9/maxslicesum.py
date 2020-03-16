def solution(A):
    # write your code in Python 3.6
    max_integer = max(A)
    max_ending = 0
    if max_integer > 0:
        max_slice = 0
    else:
        max_slice = sum(A)
    for e in A:
        max_ending = max(e, max_ending+e)
        max_slice = max(max_slice, max_ending)
    return max_slice