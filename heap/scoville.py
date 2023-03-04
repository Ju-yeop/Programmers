import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for value in scoville:
        heapq.heappush(h, value)
    while h:
        first = heapq.heappop(h)
        if first >= K:
            break
        second = heapq.heappop(h)
        new = first + second * 2
        heapq.heappush(h, new)
        if len(h) == 1 and new < K:
            return -1
        answer += 1

    return answer