from collections import deque

def solution(n, edge):
    answer = 0
    visited = [False for _ in range(n+1)]
    record = []
    mapped = [[] for _ in range(n+1)]
    for item in edge:
        mapped[item[0]].append(item[1])
        mapped[item[1]].append(item[0])
    dq = deque()
    dq.append([1, 0])
    visited[1] = True
    while dq:
        t, d = dq.popleft()
        for x in mapped[t]:
            if visited[x] is False:
                dq.append([x, d+1])
                record.append([x, d+1])
                visited[x] = True

    for i in range(len(record)):
        if record[i][1] == record[-1][1]:
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))