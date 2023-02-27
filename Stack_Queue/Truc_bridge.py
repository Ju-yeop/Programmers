from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    current_weight = 0
    q = deque()
    while truck_weights:
        if q:
            if q[0][1] == 0:
                current_weight -= q[0][0]
                q.popleft()
        time += 1
        if len(q) + 1 <= bridge_length and current_weight + truck_weights[-1] <= weight:
            t_w = truck_weights.pop()
            q.append([t_w, bridge_length])
            current_weight += t_w
        for i in range(len(q)):
            q[i][1] -= 1


    return time + bridge_length

print(solution(2, 10, [7, 4, 5, 6]))