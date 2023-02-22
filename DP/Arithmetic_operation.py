def solution(arr):
    answer = 0
    for i in reversed(range(len(arr))):
        if i % 2 == 0:
            if arr[i-1] == "-":
                answer = max(-(answer + int(arr[i])), answer - int(arr[i]))
            else: answer += int(arr[i])
    return answer

print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))