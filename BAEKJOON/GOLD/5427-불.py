from collections import deque

def bfs():
    fire_q = deque()
    sk_q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '@':
                sk_q.append([i,j])
                sk_used[i][j] = 1
            elif arr[i][j] == '*':
                fire_q.append([i,j])
                fire_used[i][j] = 1

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
    while sk_q:
        now = sk_q.popleft()
        y,x = now[0],now[1]
        if y == 0 or x == 0 or y == N-1 or x == M-1:
            return sk_used[y][x]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if sk_used[dy][dx] == 0:
                    if arr[dy][dx] != '#':
                        if fire_used[dy][dx] == 0 or fire_used[dy][dx] > sk_used[y][x] + 1:
                            sk_used[dy][dx] = sk_used[y][x] + 1
                            sk_q.append([dy,dx])
    return 'IMPOSSIBLE'
T = int(input())
for tc in range(1,T+1):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    fire_used = [[0] * M for _ in range(N)]
    sk_used = [[0] * M for _ in range(N)]
    direct_i = [-1, 0, 1, 0]
    direct_j = [0, 1, 0, -1]
    print(bfs())
