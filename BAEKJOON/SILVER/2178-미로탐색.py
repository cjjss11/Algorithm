# 1. DFS로 풀이 -> 시간 초과
N,M = map(int,input().split())
arr = [[0]*(M+2)]+[[0]+list(map(int,input()))+[0] for _ in range(N)]+[[0]*(M+2)]
used = [[0]*(M+2)]+[[0]+[0]*M+[0] for _ in range(N)]+[[0]*(M+2)]
cnt = 1
minvalue = 21e8
def dfs(y,x):
    global cnt,minvalue
    if y == N and x == M:
        if cnt < minvalue:
            minvalue = cnt
        return
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    for i in range(4):
        dy = y + direct_i[i]
        dx = x + direct_j[i]
        if 0 <= dy < (N+2) and 0 <= dx < (M+2):
            if arr[dy][dx] == 1:
                if used[dy][dx] == 0:
                    used[dy][dx] = 1
                    cnt += 1
                    dfs(dy,dx)
                    used[dy][dx] = 0
                    cnt -= 1

used[1][1] = 1
dfs(1,1)
print(minvalue)

# 2. BFS로 풀이 -> 정답
from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used = [[0]*M for _ in range(N)]
    used[y][x] = 1
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        now = q.popleft()
        now_y,now_x = now[0],now[1]
        for i in range(4):
            dy = now_y + direct_i[i]
            dx = now_x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 1:
                    if used[dy][dx] == 0:
                        q.append([dy,dx])
                        used[dy][dx] = used[now_y][now_x] + 1
                        if dy == N-1 and dx == M-1:
                            print(used[dy][dx])
bfs(0,0)