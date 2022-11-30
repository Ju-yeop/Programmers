def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    cycle = [x for x in range(n)]
    visited = [False for _ in range(n)]

    def get_parent(x):
        if cycle[x] == x:
            return x
        return get_parent(cycle[x])

    def union(x, y):
        x_p = get_parent(x)
        y_p = get_parent(y)
        if x_p > y_p: cycle[x_p] = y_p
        elif x_p < y_p: cycle[y_p] = x_p

    def judge(x, y):
        x_p = get_parent(x)
        y_p = get_parent(y)
        if x_p == y_p: return True
        else: return False

    for x, y, cost in costs:
        if judge(x, y): continue
        union(x, y)
        visited[x], visited[y] = True, True
        answer += cost

    return answer


print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))