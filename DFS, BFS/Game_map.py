from collections import deque

def solution(maps):
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    maps[-1][-1] = -1
    dq = deque()
    visited[0][0] = True
    dq.append([0, 0])
    while len(dq) != 0:
        v = dq.popleft()
        x, y = v[0], v[1]
        for i in range(4):
            m_x = x + move[i][0]
            m_y = y + move[i][1]
            if -1 < m_x < len(maps) and -1 < m_y < len(maps[0]):
                if not visited[m_x][m_y] and maps[m_x][m_y] != 0:
                    dq.append([m_x, m_y])
                    maps[m_x][m_y] = maps[x][y] + 1
                    visited[m_x][m_y] = True
    return maps[-1][-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))