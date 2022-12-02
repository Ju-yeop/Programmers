import copy

def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for temp in times:
            people += mid // temp
        if people >= n:
            end = mid - 1
        elif people < n:
            start = mid + 1
            answer = mid
    return answer + 1


def time_over(n, times):
    answer = 0
    people = len(times)
    current = copy.copy(times)
    while n > 0:
        point = min(current)
        for i in range(people):
            current[i] = current[i] - point
            if current[i] == 0:
                n -= 1
                current[i] = times[i]
        answer += point
    return answer


print(solution(6, [7, 10]))