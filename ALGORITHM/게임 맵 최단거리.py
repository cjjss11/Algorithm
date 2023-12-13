# 1. 첫 번째 방법
from collections import deque
def solution(maps):
    global answer,flag
    N = len(maps)
    M = len(maps[0])
    answer = 0
    flag = 0
    def bfs(y,x):
        global answer,flag
        q = deque()
        q.append([y,x])
        used = [[0]*M for _ in range(N)]
        direct_i = [-1,0,1,0]
        direct_j = [0,1,0,-1]
        used[y][x] = 1
        while q:
            now = q.popleft()
            y,x = now[0],now[1]
            if y == N-1 and x == M-1:
                flag = 1
                return used[y][x]
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < N and 0 <= dx < M:
                    if maps[dy][dx] == 1:
                        if used[dy][dx] == 0:
                            used[dy][dx] = used[y][x] + 1
                            q.append([dy,dx])
    result = bfs(0,0)
    if flag:
        answer = result
    else:
        answer = -1
    return answer

# 2. 두 번째 방법
from collections import deque
def solution(maps):
    answer = bfs(maps, 0, 0)
    if flag == 1:
        return answer
    else:
        return -1
    
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
flag = 0
def bfs(maps, y, x):
    global flag
    q = deque()
    q.append((y,x))
    N = len(maps)
    M = len(maps[0])
    used = [[0]*M for _ in range(N)]
    used[y][x] = 1
    while q:
        y,x = q.popleft()
        if y == N-1 and x == M-1:
            flag = 1  # 도착지점에 도달했는지 체크
            return used[y][x]
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if maps[dy][dx] == 1:
                    if used[dy][dx] == 0:
                        used[dy][dx] = used[y][x] + 1
                        q.append((dy,dx))

# 3. 세 번째 방법
from collections import deque
def solution(maps):
    q = deque()
    q.append((0,0,1))  # y좌표, x좌표, 이동 칸
    N = len(maps)
    M = len(maps[0])
    maps[0][0] = 0     # 시작 위치 방문 표시
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if dy == N-1 and dx == M-1:
                return cnt + 1
            if 0 <= dy < N and 0 <= dx < M:
                if maps[dy][dx] == 1:
                    q.append((dy,dx,cnt+1))
                    maps[dy][dx] = 0   # 방문할 위치를 미리 방문 표시
    
    return -1  # 도착지점에 도달하지 못한 경우
                