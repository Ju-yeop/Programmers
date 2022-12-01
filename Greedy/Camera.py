def solution(routes):
    answer = 0
    move = 0
    routes.sort(key=lambda x: x[1])
    for i in range(len(routes)):
        if move > i:
            continue
        move = i
        while move < len(routes) - 1:
            move = move + 1
            if routes[move][0] > routes[i][1]:
                answer += 1
                break
    return answer + 1



print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))