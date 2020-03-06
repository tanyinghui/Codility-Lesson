# Time complexity: O(N**2)
# 50%

def solution(A):
    discs = len(A)
    range_limits = []
    result = 0
    for center in range(discs):
        radius = A[center]
        lower = center-radius
        upper = center+radius
        range_limits.append([lower,upper,radius])
    range_limits.sort(key=lambda x:x[2],reverse=True)
    for i in range(discs-1):
        for e in range_limits[i+1:]:
            if range_limits[i][0] in range(e[0],e[1]+1) or range_limits[i][1] in range(e[0],e[1]+1) \
                or e[0] in range(range_limits[i][0],range_limits[i][1]+1) \
                or e[1] in range(range_limits[i][0],range_limits[i][1]+1):
                result += 1
            if result > 10000000:
                return -1
    return result