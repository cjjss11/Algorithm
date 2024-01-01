from collections import deque
N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
clean = 0
def bfs(y,x):
    global clean, d
    q = deque()
    q.append([y,x])
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        cnt = 0
        now = q.popleft()
        now_y,now_x = now[0],now[1]
        if arr[now_y][now_x] == 0:
            arr[now_y][now_x] = 2 # 청소
            clean += 1
        for i in range(4):
            dy = now_y + direct_i[i]
            dx = now_x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0:
                    cnt += 1
        if cnt == 0: # 청소되지 않은 빈칸이 없는 경우
            if d == 0: # 북쪽
                y = y + 1
            elif d == 1: # 동쪽
                x = x - 1
            elif d == 2: # 남쪽
                y = y - 1
            elif d == 3: # 서쪽
                x = x + 1
            if arr[y][x] != 1:
                q.append([y,x])
            else:
                return clean
        else: # 4칸 중 청소되지 않은 빈칸이 있는 경우
            for i in range(4):
                dr = d % 4
                if dr == 0:
                    d = 3
                    if arr[y][x-1] == 0:
                        x = x - 1
                        q.append([y,x])
                        break
                elif dr == 1:
                    d = 0
                    if arr[y-1][x] == 0:
                        y = y - 1
                        q.append([y,x])
                        break
                elif dr == 2:
                    d = 1
                    if arr[y][x+1] == 0:
                        x = x + 1
                        q.append([y,x])
                        break
                elif dr == 3:
                    d = 2
                    if arr[y+1][x] == 0:
                        y = y + 1
                        q.append([y,x])
                        break
    return clean

print(bfs(r,c))