"""분기, 뻗어 나가는 트리"""

def recursion_solution(numbers, target):
    def dfs(l, n, ls):
        nonlocal answer
        if l == len(ls):
            if n == target:
                answer += 1
            return
        v = ls[l]
        dfs(l+1, n+v, ls)
        dfs(l+1, n-v, ls)

    answer = 0
    dfs(0, 0, numbers)
    return answer

def solution(numbers, target):
    answer = 0
    ls = [0]
    for item in numbers:
        temp = []
        for j in ls:
            temp.append(j + item)
            temp.append(j - item)
        ls = temp

    for i in ls:
        if i == target:
            answer += 1

    return answer


print(solution([4, 1, 2, 1], 4))