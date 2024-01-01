for test_case in range(1, 11):
    lst = list(input().split())
    lst[0] = int(lst[0])
    answer = []
    for i in range(lst[0]):
        answer.append(lst[1][i])
    idx = 0
    while 1:
        if idx >= len(answer)-1:
            break
        if answer[idx] == answer[idx+1]:
            answer.pop(idx)
            answer.pop(idx)
            idx = 0
        else:
            idx += 1
    print(f'#{test_case}',end=' ')
    for i in answer:
        print(i,end='')
    print()
