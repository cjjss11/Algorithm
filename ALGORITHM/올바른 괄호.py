def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                answer = False
            else:
                pair = stack.pop()
                if i == ')' and pair != '(':
                    answer = False
    if len(stack) != 0:
        answer = False

    return answer