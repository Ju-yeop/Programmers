def solution(sizes):
    width, height = 0, 0
    for item in sizes:
        width = max(width, item[0], item[1])
        height = max(height, min(item[0], item[1]))
    answer = width * height
    return answer