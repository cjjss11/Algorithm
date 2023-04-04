T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = [2,3,5,7,11]
    cnt_lst = [0]*5
    for i in range(len(lst)):
        if N == 1:
            break
        cnt = 0
        while 1:
            if N % lst[i] == 0:
                cnt += 1
                N = N // lst[i]
            else:
                cnt_lst[i] = cnt
                break
    print(f'#{test_case}',end=' ')
    print(*cnt_lst)