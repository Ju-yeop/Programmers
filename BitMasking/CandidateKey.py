# def solution(relation):
#     answer = 0
#     bitLs = [0 for _ in range(len(relation[0]))]
#     new_ls = [[] for _ in range(len(relation[0]))]
#     for i in range(len(relation[0])):
#         for j in range(len(relation)):
#             new_ls[i].append(relation[j][i])
#
#     for i in range(len(new_ls)):
#         for n, item in enumerate(new_ls[i]):
#             if new_ls[i].count(item) > 1:
#                 bitLs[i] = bitLs[i] | (1 << (len(new_ls[i]) - n - 1))
#     return bitLs

from itertools import combinations
def solution(relation):
    unique = []
    idxLs = []
    for i in range(1, len(relation[0]) + 1):
        idxLs.extend(combinations(range(len(relation[0])), i))

    for i in idxLs:
        temp = [tuple(item[key] for key in i) for item in relation]
        if len(set(temp)) == len(relation):
            flag = True
            for j in unique:
                if set(j).issubset(i):
                    flag = False
                    break
            if flag: unique.append(i)
    return len(unique)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"]
                   ,["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))