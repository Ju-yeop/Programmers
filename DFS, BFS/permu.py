def solution(numbers):
    answer = []
    judge = [False for _ in range(len(numbers))]

    def perm(n, depth, w):
        if depth == n:
            answer.append(w)
            return
        if n > 0:
            for i in range(len(numbers)):
                if judge[i] is True: continue
                judge[i] = True
                perm(n, depth + 1, w + str(numbers[i]))
                judge[i] = False

    def comb(n, idx, w):
        if len(w) == n:
            answer.append(w)
            return
        for i in range(idx, len(numbers)):
            comb(n, i+1, w + str(numbers[i]))

    comb(2, 0, '')
    return answer




print(solution([1, 2, 3]))