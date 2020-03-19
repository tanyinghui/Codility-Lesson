'''
Find the number of perfect squares between two given numbers. For example, given a = 8, b = 26.
The desired output is 3 because 3**2, 4**2, 5**2.
'''
import math

def solution(a,b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 