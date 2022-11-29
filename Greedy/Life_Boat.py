def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start, end = 0, len(people) - 1
    while start <= end:
        if start == end and people[start] < limit:
            answer += 1
            return answer
        if people[start] + people[end] > limit:
            start += 1
            answer += 1
        else:
            start += 1
            end -= 1
            answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))