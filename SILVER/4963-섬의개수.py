from collections import  deque
while 1:
    w,h = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    if w == 0 and h == 0:
        break
    def bfs(y,x):
        q = deque()
        q.append([y,x])
        direct_i = [-1,-1,-1,0,1,1,1,0]
        direct_j = [-1,0,1,1,1,0,-1,-1]
        while q:
            now = q.popleft()
            y,x = now[0],now[1]
            for i in range(8):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < h and 0 <= dx < w:
                    if arr[dy][dx] == 1:
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])
    cnt = 0
    used = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                if used[i][j] == 0:
                    used[i][j] = 1
                    bfs(i,j)
                    cnt += 1
    print(cnt)