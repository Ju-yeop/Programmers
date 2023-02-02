from collections import deque
def solution(n, results):
    answer = 0
    bfs_ls = [[] for _ in range(n+1)]
    ls = [[] for _ in range(n+1)]
    for a, b in results: ls[a].append(b)
    def bfs(start):
        visited = [False for _ in range(n+1)]
        dq = deque()
        dq.append(start)
        while dq:
            x = dq.popleft()
            bfs_ls[start].append(x)
            for i in ls[x]:
                if visited[i] is False:
                    dq.append(i)
                    visited[i] = True
    for j in range(1, n+1): bfs(j)

    for v in range(1, n+1):
        judge = True
        for w in range(1, n+1):
            if w in bfs_ls[v]:
                continue
            if v not in bfs_ls[w]:
                judge = False
                break
        if judge is True: answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 모든 사람과의 관계가 연결되어 있어야 등수를 확인할 수 있다. -> BFS를 통해 각 사람들의 관계를 확인한다.
#   -> 내가 직접 연결되어 있는 사람을 제외한 사람의 관계에 내가 포함 되어 있는지 확인한다.