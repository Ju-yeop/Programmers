from itertools import combinations
def solution(relation):
    case = []
    unique = []
    for i in range(1, len(relation[0]) + 1):
        case.extend(combinations(range(len(relation[0])), i))
    for item in case:
        temp = []
        for ls in relation:
            temp.append(tuple(ls[j] for j in item))
        if len(set(temp)) == len(relation):
            flag = True
            for v in unique:
                if set(v).issubset(item):
                    flag = False
                    break
            if flag:
                unique.append(item)
    return len(unique)

"""
for case
case 별로 리스트에 추가해서 set으로 변환 했을 때 col length 와 같은지
같고 ls에 해당 case의 subset이 없다면 ls에 추가
"""


print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))