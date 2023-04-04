T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    result = []
    while 1:
        maxvalue = -21e8
        minvalue = 21e8
        for i in range(len(lst)):
            if lst[i] > maxvalue:
                maxvalue = lst[i]
            if lst[i] < minvalue:
                minvalue = lst[i]
        result.append(maxvalue)
        result.append(minvalue)
        lst.remove(maxvalue)
        lst.remove(minvalue)
        if len(result) == 10:
            break
    print(f'#{test_case}',end=' ')
    print(*result)