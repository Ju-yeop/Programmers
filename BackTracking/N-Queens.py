def n_queens(i, co):
    global answer
    n = len(co) - 1
    if promising(i, co):
        if i == n:
            answer += 1
        else:
            for v in range(1, n + 1):
                co[i + 1] = v
                n_queens(i + 1, co)


def promising(i, c):
    k = 1
    flag = True
    while k < i and flag:
        if c[k] == c[i] or abs(c[i] - c[k]) == (i - k):
            flag = False
        k += 1
    return flag

def solution(n):
    global answer
    answer = 0
    col = [0] * (n + 1)
    n_queens(0, col)
    return answer



print(solution(4))