from collections import deque
T = int(input())
for tc in range(1, T + 1):
    M,N,K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        arr[Y][X] = 1
    def bfs(y,x):
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
                if 0 <= dy < N and 0 <= dx < M:
                    if arr[dy][dx] == 1:
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])
    used = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                if used[i][j] == 0:
                    used[i][j] = 1
                    bfs(i,j)
                    cnt += 1
    print(cnt)