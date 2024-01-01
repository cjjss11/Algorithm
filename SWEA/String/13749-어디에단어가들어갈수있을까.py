T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt_lst = []
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if j == N - 1:
                    if cnt == K:
                        cnt_lst.append(cnt)
                    elif cnt != K:
                        cnt = 0
            else:
                if cnt == K:
                    cnt_lst.append(cnt)
                    cnt = 0
                elif cnt != K:
                    cnt = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if i == N - 1:
                    if cnt == K:
                        cnt_lst.append(cnt)
                    elif cnt != K:
                        cnt = 0
            else:
                if cnt == K:
                    cnt_lst.append(cnt)
                    cnt = 0
                elif cnt != K:
                    cnt = 0
    for i in cnt_lst:
        result += 1
    print(f'#{test_case} {result}')