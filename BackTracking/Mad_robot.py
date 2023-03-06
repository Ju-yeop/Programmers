from sys import stdin

# n_ls = list(map(int, stdin.readline().strip().split()))
# board = [[False for _ in range(30)] for _ in range(30)]
# path = []
# for i in range(1, 5):
#     n_ls[i] /= 100
#     if n_ls[i] != 0:
#         if i == 1: path.append("E")
#         if i == 2: path.append("W")
#         if i == 3: path.append("S")
#         if i == 4: path.append("N")
#
# ## cnt 초기화
# ## 경로 추가
# cnt = 0
# rate = 1
# result = 0
# def back(x, y, rate, cnt):
#     global result
#     board[x][y] = True
#     if cnt == n_ls[0]:
#         result += rate
#     else:
#         for p in path:
#             if p == "E" and board[x][y+1] is False:
#                 back(x, y + 1, rate * n_ls[1], cnt + 1)
#                 board[x][y+1] = False
#             elif p == "W" and board[x][y-1] is False:
#                 back(x, y - 1, rate * n_ls[2], cnt + 1)
#                 board[x][y - 1] = False
#             elif p == "S" and board[x+1][y] is False:
#                 back(x + 1, y, rate * n_ls[3], cnt + 1)
#                 board[x+1][y] = False
#             elif p == "N" and board[x-1][y] is False:
#                 back(x-1, y, rate * n_ls[4], cnt+1)
#                 board[x-1][y] = False
#
# back(15, 15, rate, cnt)
# print(result)


d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 4방향 탐색

def dfs(r, c, visited, total):
    global answer
    if len(visited) == N+1:
        answer += total
        return
    for idx in range(4):
        nr = r + d[idx][0]
        nc = c + d[idx][1]
        if (nr, nc) not in visited:
            visited.append((nr, nc))
            dfs(nr, nc, visited, total*probability[idx])
            visited.pop()

N, ep, wp, sp, np = map(int, input().split())
probability = [ep, wp, sp, np]
answer = 0

dfs(0, 0, [(0, 0)], 1)
print(answer * (0.01 ** N))