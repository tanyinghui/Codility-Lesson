'''
Given n, write an effective solution count the total of 1+2+3+...+n
'''
# Linear Time O(n)
def slow_solution(n):
    result = 0
    for i in range(n+1):
        result += i
    return result

# Constant Time
def fast_solution(n):
    return n * (n+1) // 2