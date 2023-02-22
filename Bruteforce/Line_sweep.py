from sys import stdin

n = int(stdin.readline())
ls = []
for _ in range(n): ls.append(list(map(int, stdin.readline().strip().split())))

ls.sort(key=lambda x: x[0])
start, end, result = ls[0][0], ls[0][1], 0

for s, e in ls:
    if start == s and end == e: continue
    if s <= end < e: end = e
    elif s > end:
        result += (end - start)
        start, end = s, e

print(result + (end - start))