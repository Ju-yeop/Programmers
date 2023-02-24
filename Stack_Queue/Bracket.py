def solution(s):
    stack = []
    for i in s:
        if len(stack) != 0:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        else:
            if i == ')':
                return False
            stack.append(i)
    return len(stack) == 0

print(solution("()()"))
print(solution(")()("))