from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
used = [[-1]*M for _ in range(N)]
direct_i = [1,0,-1,0]
direct_j = [0,-1,0,1]

def bfs(y,x):
    global used
    q = deque()
    q.append((y,x))
    used[y][x] = 0

    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if used[dy][dx] == -1:
                    if arr[dy][dx] != 0:
                        used[dy][dx] = used[y][x] + 1
                        q.append((dy,dx))

for i in range(N):
    for j in range(M):
        if used[i][j] == -1:
            if arr[i][j] == 2:
                bfs(i,j)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            used[i][j] = 0
        print(used[i][j],end=' ')
    print()
