def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for judge, x1, y1, x2, y2, dg in skill:
        if judge == 1:
            temp[x1][y1] -= dg
            temp[x2 + 1][y2 + 1] -= dg
            temp[x1][y2 + 1] += dg
            temp[x2+1][y1] += dg
        else:
            temp[x1][y1] += dg
            temp[x2 + 1][y2 + 1] += dg
            temp[x1][y2 + 1] -= dg
            temp[x2+1][y1] -= dg

    for i in range(len(temp)):
        for j in range(1, len(temp[0])):
            temp[i][j] += temp[i][j-1]

    for i in range(1, len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] += temp[i-1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


    # answer = 0
    # for judge, x1, y1, x2, y2, dg in skill:
    #     for i in range(x1, x2+1):
    #         for j in range(y1, y2+1):
    #             if judge == 1:
    #                 board[i][j] -= dg
    #             else:
    #                 board[i][j] += dg
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] > 0:
    #             answer += 1
    # return answer




print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
