T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt_lst = []
    cnt = 1
    for i in range(N-1):
        if lst[i+1] - lst[i] == 1:
            cnt += 1
        else:
            cnt_lst.append(cnt)
            cnt = 1
        if i + 1 == N - 1:
            cnt_lst.append(cnt)
    maxvalue = -21e8
    for i in cnt_lst:
        if i > maxvalue:
            maxvalue = i
    print(f'#{test_case} {maxvalue}')