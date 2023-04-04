from collections import deque
import copy
N = int(input())
color = [list(input()) for _ in range(N)]
change_color = copy.deepcopy(color)
for i in range(N):
    for j in range(N):
        if change_color[i][j] == 'G' or change_color[i][j] == 'R':
            change_color[i][j] = 'RG'
def bfs(y,x):
    q = deque()
    q.append([y,x])
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        now = q.popleft()
        y,x = now[0],now[1]
        if color[y][x] == 'B':
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if color[dy][dx] == 'B':
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])
        elif color[y][x] == 'R':
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if color[dy][dx] == 'R':
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])
        elif color[y][x] == 'G':
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < N:
                    if color[dy][dx] == 'G':
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])
def change_bfs(y,x):
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
            if 0 <= dy < N and 0 <= dx < N:
                if change_color[y][x] == 'RG':
                    for i in range(4):
                        dy = y + direct_i[i]
                        dx = x + direct_j[i]
                        if 0 <= dy < N and 0 <= dx < N:
                            if change_color[dy][dx] == 'RG':
                                if change_used[dy][dx] == 0:
                                    change_used[dy][dx] = 1
                                    q.append([dy,dx])

used = [[0]*N for _ in range(N)]
change_used = [[0]*N for _ in range(N)]
blue = 0
green = 0
red = 0
rg = 0
for i in range(N):
    for j in range(N):
        if color[i][j] == 'B':
            if used[i][j] == 0:
                used[i][j] = 1
                bfs(i,j)
                blue += 1
        elif color[i][j] == 'R':
            if used[i][j] == 0:
                used[i][j] = 1
                bfs(i,j)
                red += 1
        elif color[i][j] == 'G':
            if used[i][j] == 0:
                used[i][j] = 1
                bfs(i,j)
                green += 1
for i in range(N):
    for j in range(N):
        if change_color[i][j] == 'RG':
            if change_used[i][j] == 0:
                change_used[i][j] = 1
                change_bfs(i,j)
                rg += 1

print(f'{blue+red+green} {blue+rg}')