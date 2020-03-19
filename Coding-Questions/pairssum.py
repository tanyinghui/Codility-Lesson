'''
Given an integer array A and integer k, find pairs of numbers which add up to a given number.
For example, given A = [-8,45,1,9,4,6], k = 10
Find the pairs in A where the sum of pair equals to 10. The desired output is [(9, 1), (6, 4)].
'''

def solution(A,k):
    data  = set()
    result = []
    for e in A:
        d = k - e
        if d in data:
            result.append((e,d))
        data.add(e)
    return result

solution([-8,45,1,9,4,6],10)