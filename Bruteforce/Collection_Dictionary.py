from itertools import product

def solution(word):
    ls = ['A', 'E', 'I', 'O', 'U']
    all_data = []
    for i in range(5):
        for per in product(ls, repeat=i):
            all_data.append(''.join(per))
    all_data.sort()
    return all_data.index(word) + 1