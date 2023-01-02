def solution(answers):
    answer = []
    candidate = ['12345' * 2000, '21232425' * 1250, '3311224455' * 1000]
    mid_aw = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == int(candidate[j][i]):
                mid_aw[j] += 1
    mn = max(mid_aw)
    for i in range(3):
        if mid_aw[i] == mn:
            answer.append(i+1)
    return answer


test = solution([1, 2, 3, 4, 5])