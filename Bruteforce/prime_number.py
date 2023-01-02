from itertools import permutations
def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        candidate = list(set(permutations(list(numbers), i+1)))
        for item in candidate:
            if item[0] == '0': continue
            convertInt = int(''.join(list(item)))
            if convertInt != 1:
                judge = True
                for k in range(2, convertInt):
                    if convertInt % k == 0:
                        judge = False
                        break
                if judge is True:
                    answer += 1

    return answer


test = solution("011")