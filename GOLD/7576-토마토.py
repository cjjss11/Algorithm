from collections import deque
M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
def bfs():
    q = deque()
    used = [[0]*M for _ in range(N)]
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                if used[y][x] == 0:
                    used[y][x] = 1
                    q.append([y,x])
    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0:
                    used[dy][dx] = used[y][x] + 1
                    arr[dy][dx] = 1
                    q.append([dy,dx])
    return used[y][x] - 1
ans = bfs()
flag = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = 1
if flag:
    print(-1)
else:
    print(ans)