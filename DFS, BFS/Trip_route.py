from collections import deque

def solution(tickets):
    answer = []
    visited = [False for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])
    print(tickets)

    def dfs(v):
        answer.append(v)
        if len(answer) == len(tickets) + 1:
            return answer
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == v:
                visited[i] = True
                dfs(tickets[i][1])
                visited[i] = False
                if len(answer) != len(tickets) + 1:
                        answer.pop()

    dfs('ICN')
    return answer


print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))