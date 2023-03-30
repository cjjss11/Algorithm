from collections import deque
M,N,H = map(int,input().split()) # M은 가로 N은 세로 H는 상자 수
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
def bfs():
    q = deque()

    direct_h = [0, 0, 0, 0, -1, 1]
    direct_i = [-1, 0, 1, 0, 0, 0]
    direct_j = [0, 1, 0, -1, 0, 0]
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if arr[h][y][x] == 1:  # 익은 토마토이고
                    if used[h][y][x] == 0:  # 방문한 적 없으면
                        used[h][y][x] = 1  # 1 체크
                        q.append([h,y,x])
    while q:
        now = q.popleft()
        h,y,x = now[0],now[1],now[2]
        for i in range(6):
            dh = h + direct_h[i]
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
                if arr[dh][dy][dx] == 0: # 안 익은 토마토이고
                    if used[dh][dy][dx] == 0: # 방문한 적 없으면
                        arr[dh][dy][dx] = 1 # 익은 토마토로 바꿔주고
                        used[dh][dy][dx] = used[h][y][x] + 1 # 날짜 + 1
                        q.append([dh,dy,dx])
    return used[h][y][x] - 1

used = [[[0] * M for _ in range(N)] for _ in range(H)]
ans = bfs()
flag = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0: # 다 끝났는데 안 익은 토마토가 있으면
                flag = 1
if flag:
    print(-1)
else:
    print(ans)