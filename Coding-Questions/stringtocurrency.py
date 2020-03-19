'''Format a string of numbers to display a currency - example" "1234.678" to "1,234.68".
'''
def solution(S):
    currency = float("{0:.2f}".format(float(S)))
    currency = list(str(currency))
    n = len(currency)
    count = 0
    for i in range(n-2,-1,-1):
        count += 1
        if count % 3 == 0 and count != 3:
            currency[i] = currency[i] + ','
    return ''.join(currency)