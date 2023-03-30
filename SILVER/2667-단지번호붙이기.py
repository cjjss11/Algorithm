from collections import deque
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
used = [[0]*N for _ in range(N)]
result = []
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used[y][x] = 1
    cnt = 1
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        now = q.popleft()
        now_y,now_x = now[0],now[1]
        for i in range(4):
            dy = now_y + direct_i[i]
            dx = now_x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < N:
                if used[dy][dx] == 0:
                    if arr[dy][dx] == 1:
                        q.append([dy,dx])
                        used[dy][dx] = 1
                        cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if used[i][j] == 0:
                result.append(bfs(i,j))
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])