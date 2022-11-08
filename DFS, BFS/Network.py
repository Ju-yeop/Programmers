from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    def dfs(v):
        visited[v] = True
        for q in range(len(ls[v])):
            if not visited[q] and computers[v][q] == 1:
                dfs(q)

    for u in range(n):
        if not visited[u]:
            answer += 1
            dfs(u)

    return answer


print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 1, 1]]))
