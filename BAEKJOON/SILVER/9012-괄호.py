N = int(input())
for _ in range(N):
    lst = list(input())
    stack = []
    def check():
        for i in lst:
            if i == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return 0
                else:
                    pair = stack.pop()
                    if i == ')' and pair != '(':
                        return 0
        if len(stack) != 0:
            return 0
    answer = check()
    if answer == 0:
        print('NO')
    else:
        print('YES')
