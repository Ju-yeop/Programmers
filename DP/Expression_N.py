def solution(N, number):
    ls = [[] for _ in range(9)]
    for i in range(1, 9):
        ls[i].append(int(str(N) * i))
        if int(str(N) * i) == number: return i
    for i in range(2, 9):
        for j in range(1, i):
            div1 = j  #연산자
            div2 = i-j  #피연산자
            for v in ls[div1]:
                for w in ls[div2]:
                    temp = [v+w, v*w, v//w, v-w, w//v, w-v]
                    if number in temp: return i
                    while 0 in temp: temp.remove(0)
                    ls[i].extend(temp)
    return -1


print(solution(5, 12))