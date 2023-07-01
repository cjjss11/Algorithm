from collections import deque
N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]

def bfs(y,x):
    used = [[0] * M for _ in range(N)]
    used[y][x] = 1
    q = deque()
    q.append([y,x,0])
    while q:
        y,x,time = q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 'L':
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        q.append([dy,dx,time+1])
    return time

max_distance = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            max_distance = max(max_distance,bfs(i,j))
print(max_distance)
