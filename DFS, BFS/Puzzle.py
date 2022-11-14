from collections import deque

def solution(game_board, table):
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            game_board[i][j] = not game_board[i][j]
    answer = 0

    def rotation(ls):
        l = len(ls)
        k = len(ls[0])
        frame = [[0 for _ in range(l)] for _ in range(k)]
        for i in range(k):
            for j in range(l):
                frame[i][j] = ls[l-j-1][i]
        return frame

    def extraction(ls, x, y, visit):
        puzzle_location = []
        dq = deque()
        dq.append([x, y])
        visit[x][y] = True
        while len(dq) != 0:
            v = dq.popleft()
            w, h = v[0], v[1]
            puzzle_location.append([w, h])
            for i in range(4):
                m_w = w + move[i][0]
                m_h = h + move[i][1]
                if -1 < m_w < len(ls) and -1 < m_h < len(ls):
                    if not visit[m_w][m_h] and ls[m_w][m_h] == 1:
                        dq.append([m_w, m_h])
                        visit[m_w][m_h] = True
        return puzzle_location
    """
    한 칸(퍼즐)에 대해 BFS
    """

    def trans_puzzle(puzzle_location):
        x_min, x_max = 100, -1
        y_min, y_max = 100, -1
        for x, y in puzzle_location:
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            y_min = min(y_min, y)
            y_max = max(y_max, y)
        x_size = x_max - x_min + 1
        y_size = y_max - y_min + 1
        puzzle = [[0 for _ in range(y_size)] for _ in range(x_size)]
        for x, y in puzzle_location:
            puzzle[x-x_min][y-y_min] = 1
        return puzzle


    table_puzzles = []
    visited = [[False for _ in range(51)] for _ in range(51)]
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1 and visited[i][j] is False:
                temp = []
                location = extraction(table, i, j, visited)
                pz = trans_puzzle(location)
                temp.append(pz)
                for _ in range(3):
                    pz = rotation(pz)
                    temp.append(pz)
                table_puzzles.append(temp)

    game_visited = [[False for _ in range(len(game_board))] for _ in range(len(game_board))]
    table_puzzles_visited = [False for _ in range(len(table_puzzles))]
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 1 and game_visited[i][j] is False:
                location = extraction(game_board, i, j, game_visited)
                pz = trans_puzzle(location)
                for n, v in enumerate(table_puzzles):
                    judge = False
                    if table_puzzles_visited[n] is False:
                        for w in range(len(v)):
                            if v[w] == pz:
                                for p in pz:
                                    for q in p:
                                        if q == 1:
                                            answer += 1
                                table_puzzles_visited[n] = True
                                judge = True
                                break
                    if judge is True:
                        break


    return answer



"""
Game board 0,0 부터 for문 퍼즐 빈칸 하나를 찾으면 extraction -> trans_puzzle => Table_puzzle Array와 비교
table의 모든 퍼즐을 추출해서 배열 형태로 미리 저장(회전 포함) = table_puzzle Array
"""



print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))