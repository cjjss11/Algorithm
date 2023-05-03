from collections import deque
M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    direct_i = [-1,-1,0,1,1,1,0,-1]
    direct_j = [0,1,1,1,0,-1,-1,-1]
    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        for i in range(8):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < M and 0 <= dx < N:
                if arr[dy][dx] == 1:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        q.append([dy,dx])

cnt = 0
used = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            if used[i][j] == 0:
                used[i][j] = 1
                bfs(i,j)
                cnt += 1
print(cnt)