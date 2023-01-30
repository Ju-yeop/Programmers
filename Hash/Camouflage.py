"""
from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = 0
    dic = defaultdict(int)
    for item in clothes:
        dic[item[1]] += 1
    for i in range(1, len(dic.keys()) + 1):  
        ls = list(combinations(dic.values(), i))
        for item in ls:
            answer += multi(item)
    return answer


def multi(arr):
    temp = 1
    for i in arr:
        temp *= i
    return temp
"""

from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for item in clothes:
        dic[item[1]] += 1
    for i in dic.values():
        answer *= i+1
    return answer-1