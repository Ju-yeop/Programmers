import copy

def solution(progresses, speeds):
    result = []
    final = []
    for i in range(len(progresses)):
        value = progresses[i]
        cnt = 0
        while value < 100:
            value += speeds[i]
            cnt += 1
        result.append(cnt)
    x = result[0]
    answer = 0
    while result:
        temp = result.pop(0)
        if temp <= x:
            answer += 1
        else:
            final.append(answer)
            answer = 1
            x = temp

    final.append(answer)
    return final
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))