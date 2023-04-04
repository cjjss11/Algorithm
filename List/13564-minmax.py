T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    maxvalue = lst[0]
    minvalue = lst[0]
    for i in lst:
        if i > maxvalue:
            maxvalue = i
        if i < minvalue:
            minvalue = i
    print(f'#{test_case} {maxvalue-minvalue}')