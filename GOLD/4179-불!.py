from collections import deque
N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
fire_used = [[0]*M for _ in range(N)]
jh_used = [[0]*M for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]

def bfs():
    fire_q = deque()
    jh_q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'F': # 불 좌표 담기
                fire_q.append([i,j])
                fire_used[i][j] = 1
            elif arr[i][j] == 'J': # 지훈이 위치 담기
                jh_q.append([i,j])
                jh_used[i][j] = 1
    while fire_q: 
        now = fire_q.popleft()
        y,x = now[0],now[1]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if fire_used[dy][dx] == 0:
                    if arr[dy][dx] != '#':
                        fire_used[dy][dx] = fire_used[y][x] + 1
                        fire_q.append([dy,dx])
    while jh_q:
        now = jh_q.popleft()
        y,x = now[0],now[1]
        if y == 0 or x == 0 or y == N-1 or x == M-1: # 가장자리 좌표
            return jh_used[y][x]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if jh_used[dy][dx] == 0:
                    if arr[dy][dx] != '#':
                        # 제일 중요한 코드!!
                        if fire_used[dy][dx] == 0 or fire_used[dy][dx] > jh_used[y][x] + 1:
                            jh_used[dy][dx] = jh_used[y][x] + 1
                            jh_q.append([dy,dx])
    return 'IMPOSSIBLE'
print(bfs())