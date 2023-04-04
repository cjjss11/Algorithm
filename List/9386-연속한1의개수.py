T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input()))
    cnt_lst = []
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            cnt += 1
            if i == len(lst)-1:
                cnt_lst.append(cnt)
        elif lst[i] == 0:
            if cnt != 0:
                cnt_lst.append(cnt)
                cnt = 0
            else:
                continue
    maxvalue = -21e8
    for i in cnt_lst:
        if i > maxvalue:
            maxvalue = i
    print(f'#{test_case} {maxvalue}')