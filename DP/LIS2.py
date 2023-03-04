from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
ls = list(map(int, stdin.readline().strip().split()))
dp = [1]
lis = [ls[0]]
for i in range(1, len(ls)):
    if lis[-1] < ls[i]:
        dp.append(dp[-1] + 1)
        lis.append(ls[i])
    else:
        idx = bisect_left(lis, ls[i])
        lis[idx] = ls[i]
print(lis)