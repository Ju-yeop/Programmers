from sys import stdin

n, m = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().strip().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    dif = 0
    for i in range(n):
        if arr[i] > mid:
            dif += (arr[i] - mid)

    if dif == target:
        return mid
    elif dif > target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)

print(binary_search(tree, m, 0, max(tree)-1))
