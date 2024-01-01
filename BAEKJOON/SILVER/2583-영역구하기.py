from collections import deque
M,N,K = map(int,input().split())
arr = [[0]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1

def bfs(y,x):
    cnt = 1
    q = deque()
    q.append([y,x])
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < M and 0 <= dx < N:
                if arr[dy][dx] == 0:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        cnt += 1
                        q.append([dy,dx])
    return cnt

result = []
used = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            if used[i][j] == 0:
                used[i][j] = 1
                ans = bfs(i,j)
                result.append(ans)
answer = sorted(result, key=lambda x:x)
print(len(answer))
print(*answer)