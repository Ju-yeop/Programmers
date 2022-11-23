def solution(name):
    answer = 0
    num_list = [min(abs(ord('A') - ord(n)), 26 - abs(ord('A') - ord(n))) for n in name]
    answer += sum(num_list)
    min_move = len(name) - 1

    for i, item in enumerate(name):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min(min_move, 2*i + len(name)-next, 2*(len(name)-next) + i)

    return answer + min_move