import heapq as hq


def solution(operations):
    def del_max(mx_h, mi_h):
        if len(mx_h) > 0:
            p = -hq.heappop(mx_h)
            mi_h.remove(p)
            hq.heapify(mi_h)
            return p

    def del_min(mx_h, mi_h):
        if len(mx_h) > 0:
            p = hq.heappop(mi_h)
            mx_h.remove(-p)
            hq.heapify(mx_h)
            return p

    answer = []
    max_heap = []
    min_heap = []
    for item in operations:
        op, v = item.split(' ')
        if op == 'I':
            hq.heappush(max_heap, -int(v))
            hq.heappush(min_heap, int(v))
        else:
            if v == '1':
                del_max(max_heap, min_heap)
            elif v == "-1":
                del_min(max_heap, min_heap)
    if len(max_heap) == 0:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]

print(solution(["I 6", "I 2", "I 1", "I 4", "I 5", "I 3", "D 1", "I 7", "D -1", "I 6", "D -1", "D -1"]))