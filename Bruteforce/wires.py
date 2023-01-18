import copy
from collections import deque

#자식 노드의 개수를 구해서 자르기 - 깊이 구해서 야심차게 했지만 실패...
def bfsDepth(n, wires):
    visited = [False for _ in range(n+1)]
    count = [1 for _ in range(n+1)]
    dq = deque()
    dq.append([1, 1])
    visited[1] = True
    container = []
    while dq:
        t, depth = dq.popleft()
        container.append([t, depth])
        visited[t] = True
        for x, y in wires:
            if x == t and visited[y] is False:
                dq.append([y, depth + 1])
                for i, con_depth in container:
                    if con_depth != depth or i == t:
                        count[i] += 1
            elif y == t and visited[x] is False:
                dq.append([x, depth + 1])
                for i, con_depth in container:
                    if con_depth != depth or i == t:
                        count[i] += 1
    flag = n/2
    check = copy.copy(count)
    for i in range(len(count)):
        count[i] = abs(count[i] - flag)
    index = count.index(min(count))
    return n - check[index] -check[index]


#전선 하나씩 다 끊어 가면서 BFS
def bfsBruteforce(n, wires):
    def bfs(start):
        visited = [False for _ in range(n+1)]
        dq = deque()
        dq.append(start)
        result = 1
        while dq:
            x = dq.popleft()
            visited[x] = True
            for i in graph[x]:
                if visited[i] is False:
                    dq.append(i)
                    result += 1
        return result

    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(answer, abs(bfs(a) - bfs(b)))

        graph[a].append(b)
        graph[b].append(a)

    return answer


#유니온 파인드
def UnionFind(n, wires):
    def find(x, parent):
        if parent[x] != x:
            return find(parent[x], parent)
        return parent[x]

    def union(a, b, parent):
        a_p = find(a, parent)
        b_p = find(b, parent)

        if a_p < b_p:
            parent[b_p] = a_p
        else: parent[a_p] = b_p

    parent = [0 for _ in range(n+1)]
    for i in range(len(parent)):
        parent[i] = i

    answer = n
    for i in range(len(wires)):
        co_wires = copy.deepcopy(wires)
        co_parent = copy.deepcopy(parent)
        co_wires.pop(i)
        for x, y in co_wires:
            union(x, y, co_parent)
        for p, q in co_wires:
            co_parent[p] = find(co_parent[p], co_parent)
            co_parent[q] = find(co_parent[q], co_parent)
        answer = min(answer, abs(co_parent.count(co_parent[wires[i][0]]) - co_parent.count(co_parent[wires[i][1]])))
        co_wires.append([wires[i][0], wires[i][1]])

    return answer






print(UnionFind(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(bfsBruteforce(4, [[1,2],[2,3],[3,4]]))