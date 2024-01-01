T = int(input())
for test_case in range(1, T + 1):
    lst = list(input())
    stack = []
    def check():
        for i in lst:
            if i in '[{(':
                stack.append(i)
            elif i in ']})':
                if len(stack) == 0:
                    return 0
                else:
                    pair = stack.pop()
                    if i == ')' and pair != '(' or i == '}' and pair != '{' or i == ']' and pair != '[':
                        return 0
        if len(stack) > 0:
            return 0
    result = check()
    if result == 0:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {1}')