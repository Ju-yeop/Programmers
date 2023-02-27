def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        current_value = prices[i]
        for j in range(i+1, len(prices)):
            if current_value <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

print(solution([1, 2, 3, 2, 3]))