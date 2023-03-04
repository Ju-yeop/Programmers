import heapq as hq

def solution(jobs):
    l = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    answer = 0
    time = 0
    active = False
    h = []
    while True:
        while jobs and jobs[0][0] == time:
            x, y = jobs.pop(0)
            hq.heappush(h, [y, x])
        if active is False and h:
            dur, s = hq.heappop(h)
            active = True
            con = time + dur
            answer += (con - s)
        if active is True and time == con - 1:
            active = False
        if active is False and not h and not jobs:
            break
        time += 1

    return answer // l

print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))