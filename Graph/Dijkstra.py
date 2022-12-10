import sys

N = 7
s = 3
g = [[] for _ in range(N)]

g[0] = [(1, 9), (2, 10)]
g[1] = [(0, 9), (3, 10), (4, 5), (6, 3)]
g[2] = [(0, 10), (3, 9), (4, 7), (5, 2)]
g[3] = [(1, 10), (2, 9), (5, 4), (6, 8)]
g[4] = [(1, 5), (2, 7), (6, 1)]
g[5] = [(2, 2), (3, 4), (6, 6)]
g[6] = [(1, 3), (3, 8), (4, 1), (5, 6)]

previous = [None] * N
D = [sys.maxsize] * N
visited = [False] * N
previous[s] = s
D[s] = 0

for i in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True

    for w, wt in list(g[m]):
        if not visited[w]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt
                previous[w] = m

print('정점 %d로부터의 최단 거리' %s)
for k in range(N):
    if k == s: continue
    if D[k] == sys.maxsize: print('(%d, %d)는 연결되어 있지 않습니다.' % (s, k))
    else:
        print("(%d, %d) = %d" % (s, k, D[k]))

for v in range(N):
    if v == s: continue
    if D[v] == sys.maxsize: print('(%d, %d)는 연결되어 있지 않습니다.' % (s, v))
    else:
        back = v
        print(back, end='')
        while back != s:
            print(" <- ", previous[back], end='')
            back = previous[back]
        print()