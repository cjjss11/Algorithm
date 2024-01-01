from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = 0
    def bfs(y, x):
        global flag
        q = deque()
        q.append([y, x])
        used = [[0] * N for _ in range(N)]
        used[y][x] = 1
        direct_i = [-1,0,1,0]
        direct_j = [0,1,0,-1]
        while q:
            now = q.popleft()
            y, x = now[0], now[1]
            if y == ey and x == ex:
                flag = 1
                return
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if arr[dy][dx] == '0':
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy, dx])
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '3':
                ey, ex = i, j
                arr[i][j] = '0'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                bfs(i,j)
    if flag:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')