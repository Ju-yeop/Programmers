from sys import stdin

n, m, k = map(int, stdin.readline().strip().split())
ls = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= (idx & -idx)
    return result

def change_prefix(idx, dif):
    while idx <= n:
        tree[idx] += dif
        idx += (idx & -idx)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    ls[i] = int(stdin.readline())
    change_prefix(i, ls[i])

for _ in range(m+k):
    a, b, c = map(int, stdin.readline().strip().split())
    if a == 1:
        change_prefix(b, c - ls[b])
        ls[b] = c
    else:
        print(interval_sum(b, c))