from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        temp = False
        if i == location: temp = True
        q.append(([priorities[i], temp]))

    while q:
        v, key = q.popleft()
        try:
            if max(q, key=lambda x: x[0])[0] <= v:
                answer += 1
                if key is True: return answer
            else:
                q.append([v, key])
        except:
            return answer + 1


print(solution([2, 1, 3, 2], 2))
