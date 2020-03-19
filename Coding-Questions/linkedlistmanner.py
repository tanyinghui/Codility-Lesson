'''
A non-empty zero-indexed array A consisting of N integers is given.
Array A represents a linked list. A list is constructed from this array as follows:

• the first node (the head) is located at index 0;
• the value of a node located at index K is A[K];
• the successor of a node located at index K is located at index A[K];
• if the value of a node is −1 then it is the last node of the list. For example, for array A such that: 
    A[0] = 1
    A[1] = 4
    A[2] = -1
    A[3] = 3
    A[4] = 2

The following list is constructed:

• the first node (the head) is located at index 0 and has a value of 1;
• the second node is located at index 1 and has a value of 4;
• the third node is located at index 4 and has a value of 2;
• the fourth node is located at index 2 and has a value of −1.

Write a function:

def solution

that, given a non-empty zero-indexed array A consisting of N integers, returns the length of the list constructed from A in the above manner.
For example, given array A such that:
    A[0] = 1
    A[1] = 4
    A[2] = -1
    A[3] = 3
    A[4] = 2
the function should return 4, as explained in the example above.

The below are the assumptions that helps you to solve the problem:
• N is an integer within the range [1..200,000];
• each element of array A is an integer within the range [−1..200,000];
• it will always be possible to construct the list and its length will be finite.
'''
def solution(A):
    if -1 not in A:
        return len(A)
    else:
        result = [A[0]]
        s = A[0]
        while s != -1:
            value = A[s]
            result.append(value)
            s = value
        return len(result)