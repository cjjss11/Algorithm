while 1:
    S = input()
    if S == '.':
        break
    stack = []
    def check():
        for i in S:
            if i in '({[':
                stack.append(i)
            elif i in ')}]':
                if len(stack) == 0:
                    return 0
                else:
                    pair = stack.pop()
                    if i == ')' and pair != '(' or i == '}' and pair != '{' or i == ']' and pair != '[':
                        return 0
        if len(stack) != 0:
            return 0
    answer = check()
    if answer == 0:
        print('no')
    else:
        print('yes')