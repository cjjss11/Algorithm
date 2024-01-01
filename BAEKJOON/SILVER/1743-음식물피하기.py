from collections import deque
N,M,K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
def bfs(y,x):
    q = deque()
    q.append([y,x])
    direct_i =[-1,0,1,0]
    direct_j = [0,1,0,-1]
    cnt = 1
    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 1:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        cnt += 1
                        q.append([dy,dx])
    return cnt
maxvalue = -21e8
used = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            if used[i][j] == 0:
                used[i][j] = 1
                ans = bfs(i,j)
                if ans > maxvalue:
                    maxvalue = ans
print(maxvalue)
