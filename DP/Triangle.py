def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        for idx in range(len(triangle[i]) - 1):
            triangle[i-1][idx] += max(triangle[i][idx], triangle[i][idx+1])
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))