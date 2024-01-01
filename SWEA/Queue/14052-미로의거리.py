from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    flag = 0
    def bfs(y,x):
        q = deque()
        q.append([y,x])
        direct_i = [-1,0,1,0]
        direct_j = [0,1,0,-1]
        while q:
            global flag
            now = q.popleft()
            y,x = now[0],now[1]
            if y == ey and x == ex:
                flag = 1
                return used[y][x] - 1
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if arr[dy][dx] == 0:
                        if used[dy][dx] == 0:
                            used[dy][dx] = used[y][x] + 1
                            q.append([dy,dx])

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3: # 도착인 3인 곳을 찾고
                ey,ex = i,j  # 좌표를 저장하고
                arr[i][j] = 0 # 0으로 바꿔주기

    used = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                if used[i][j] == 0:
                    ans = bfs(i,j)
    if flag:
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case} {0}')