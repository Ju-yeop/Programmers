import copy
from collections import defaultdict


def solution(genres, plays):
    answer = []
    result = []
    dic = defaultdict(int)
    for i in range(len(genres)):
        dic[genres[i]] += plays[i]
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_dic:
        temp = defaultdict(int)
        for v in range(len(genres)):
            if genres[v] == key:
                temp[v] = plays[v]
        answer.append(temp)
    for r_dict in answer:
        sorted_r_dict = sorted(r_dict.items(), key=lambda x: x[1], reverse=True)
        for p in range(2):
            if len(sorted_r_dict) > p:
                result.append(sorted_r_dict[p][0])
    return result


print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))
