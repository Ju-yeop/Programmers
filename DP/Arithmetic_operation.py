def solution(arr):
    minmax = [0, 0]
    sum_value = 0
    for i in reversed(range(len(arr))):
        if arr[i] == "+":
            continue
        elif arr[i] == "-":
            mi, mx = minmax
            minmax[0] = min(-sum_value + mi, -(sum_value + mx))
            minmax[1] = max(-int(arr[i+1]) + (sum_value - int(arr[i+1])) + mx, -(sum_value + mi))
            sum_value = 0
        else:
            sum_value += int(arr[i])
    minmax[1] += sum_value
    return minmax[1]

print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))