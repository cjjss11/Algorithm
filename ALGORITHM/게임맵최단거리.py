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
                