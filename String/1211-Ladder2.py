for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    direct_i = [0,0,1]
    direct_j = [-1,1,0]
    used = [[0]*100 for _ in range(100)]
    cnt = 1
    cnt_lst = [0]*100
    def dfs(y,x,idx):
        global cnt
        if y == 99:
            cnt_lst[idx] = cnt
            cnt = 1
            return
        for i in range(3):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < 100 and 0 <= dx < 100:
                if arr[dy][dx] == 1:
                    if dx == x - 1 or dx == x + 1:
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            cnt += 1
                            dfs(dy,dx,idx)
                            used[dy][dx] = 0
                            break
                    else:
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            cnt += 1
                            dfs(dy,dx,idx)
                            used[dy][dx] = 0
                            break
    minvalue = 21e8
    idx = 0
    result = 0
    for i in range(100):
        if arr[0][i] == 1:
            used[0][i] = 1
            idx = i
            dfs(0,i,idx)
    for i in range(len(cnt_lst)):
        if cnt_lst[i] != 0:
            if cnt_lst[i] < minvalue:
                minvalue = cnt_lst[i]
                result = i
    print(f'#{T} {result}')