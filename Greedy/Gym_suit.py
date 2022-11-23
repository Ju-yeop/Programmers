"""5	[2, 4]	[1, 3, 5]	5"""
import copy


def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    temp = copy.copy(lost)
    for tem in temp:
        if tem in reserve:
            lost.remove(tem)
            reserve.remove(tem)

    for item in lost:
        for j in range(len(reserve)):
            if reserve[j]-1 <= item <= reserve[j]+1:
                reserve.pop(j)
                answer += 1
                break
    return n - len(lost) + answer


print(solution(7, [2, 3, 4], [1, 2, 3, 6]))