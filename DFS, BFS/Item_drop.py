from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    ls = [[0 for _ in range(101)] for _ in range(101)]
    visited = [[False for _ in range(101)] for _ in range(101)]
    for arr in rectangle:
        for i in range(arr[0]*2, arr[2]*2+1):
            for j in range(arr[1]*2, arr[3]*2+1):
                ls[i][j] = 1

    for arr in rectangle:
        for i in range(arr[0]*2+1, arr[2]*2):
            for j in range(arr[1]*2+1, arr[3]*2):
                ls[i][j] = 0

    dq = deque()
    dq.append([characterX*2, characterY*2])
    visited[characterX*2][characterY*2] = True
    while len(dq) != 0:
        w = dq.popleft()
        x, y = w[0], w[1]
        for i in range(4):
            m_x = x + move[i][0]
            m_y = y + move[i][1]
            if -1 < m_x < 101 and -1 < m_y < 101:
                if visited[m_x][m_y] is False and ls[m_x][m_y] == 1:
                    dq.append([m_x, m_y])
                    ls[m_x][m_y] = ls[x][y] + 1

    return ls[itemX*2][itemY*2] // 2


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))