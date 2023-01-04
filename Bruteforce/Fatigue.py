def solution(k, dungeons):
    answer = []
    lg = len(dungeons)

    def dfs(n, depth, k):
        if depth == n:
            answer.append(depth)
        for i in range(n):
            if visited[i] is False:
                if dungeons[i][0] <= k:
                    visited[i] = True
                    dfs(n, depth + 1, k - dungeons[i][1])
                    visited[i] = False
                else:
                    answer.append(depth)
    for i in range(lg):
        visited = [False for _ in range(lg)]
        visited[i] = True
        if k >= dungeons[i][1]:
            dfs(lg, 1, k-dungeons[i][1])

    return max(answer)

# from collections import deque
#
#
# def bfs(start, k, dungeons):
#     queue = deque()
#     queue.append([start, k, 0, [False for _ in range(len(dungeons))]])
#     counted = []
#
#     while queue:
#         location, tired, count, visited = queue.popleft()
#         visited[location] = True
#         tired -= dungeons[location][1]
#         count += 1
#         counted.append(count)
#
#         for i in range(len(dungeons)):
#             if not visited[i] and tired >= dungeons[i][0]:
#                 queue.append([i, tired, count, visited[:]])
#
#     return max(counted)
#
#
# def solution(k, dungeons):
#     answer = -1
#     for i in range(len(dungeons)):
#         if dungeons[i][0] <= k:
#             answer = max(answer, bfs(i, k, dungeons))
#     return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
