from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [False for _ in range(len(words))]
    dq = deque()
    dq.append([0, begin])
    while len(dq) != 0:
        w = dq.popleft()
        depth, v = w[0], w[1]
        if v == target:
            return depth
        for index, item in enumerate(words):
            spell_count = 0
            for spell_index in range(len(item)):
                if item[spell_index] == v[spell_index]:
                    spell_count += 1
            if spell_count == len(item)-1 and visited[index] is False:
                dq.append([depth+1, item])
                visited[index] = True
    return 0


print(solution("aab", "aba", ["abb", "aba"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))