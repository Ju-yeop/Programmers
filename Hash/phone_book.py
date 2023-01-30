# from collections import defaultdict
#
# def solution(phone_book):
#
#     phone_book.sort()
#     dict = defaultdict(int)
#     for item in phone_book:
#         for k in dict.keys():
#             if k == item[0:len(k)]:
#                 return False
#         dict[item] = 1
#     return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] < phone_book[i+1]:
            if phone_book[i+1][0:len(phone_book[i])] == phone_book[i]:
                return False
    return True