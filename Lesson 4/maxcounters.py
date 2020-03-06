def solution(N, A):
    output = [0]*N
    max_counter = 0
    current_max = 0
    for e in A:
        if 1 <= e <= N:
            if max_counter > output[e-1]:
                output[e-1] = max_counter
            output[e-1] += 1
            if current_max < output[e-1]:
                current_max = output[e-1]
        else:
            max_counter = current_max
    for i in range(N):
        if output[i] < max_counter:
            output[i] = max_counter
    return output