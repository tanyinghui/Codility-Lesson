'''
Given an array of N integers, find the longest leading fragment of the array which contains equal no. of X and Y. 
Expected time complexity is O(n).
For example:
A =  [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7] 
x = 7
y = 42

The expected output is 9 since at position 9 of the list gives the longest fragment of array consists of same number 
of X and Y.
'''

def solution(A,x,y):
    counter_x = counter_y = 0
    n = len(A)
    result = 0
    for k in range(n):
        if A[k] == x:
            counter_x += 1
        elif A[k] == y:
            counter_y += 1
        if counter_x != 0 and (counter_x == counter_y):
            result = k
    return result