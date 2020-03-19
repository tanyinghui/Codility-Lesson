'''
Given two arrays A and B which represent decimal numbers X and Y respectively in base -2.
Find the return value of X+Y in base -2, list form.
'''

def solution(A, B):
    # write your code in Python 3.6
    x_str = ''.join(str(e) for e in A)
    y_str = ''.join(str(e) for e in B)
    x_dec = convert_to_decimal(x_str)
    y_dec = convert_to_decimal(y_str)
    sum_dec = x_dec + y_dec
    sum_negbase = convert_to_neg(sum_dec)
    return sum_negbase

def convert_to_decimal(s):
    if s == "0":
        return 0
    output = 0
    for i, k in enumerate(s):
        output += int(k) * (-2)**i
    return output
    
def convert_to_neg(n):
    if n == 0:
        return [0]
    output = []
    while n != 0:
        n, r = divmod(n,-2)
        if r < 0:
            n += 1
            r -= -2
        output.append(r)
    return output