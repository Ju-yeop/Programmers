def solution(brown, yellow):
    answer = []
    cnt = brown + yellow
    for i in range(1, cnt//2):
        if cnt % i == 0:
            a, b = i, cnt // i
            if a*2 + b*2 - 4 == brown:
                answer = [a, b]
    return answer