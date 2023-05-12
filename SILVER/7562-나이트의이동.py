from collections import deque
T = int(input())
for tc in range(1, T+1):
    L = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    used = [[0] * L for _ in range(L)]
    def bfs(sy,sx,ey,ex):
        q = deque()
        q.append((sy,sx))
        direct_i = [-2,-1,1,2,2,1,-1,-2]
        direct_j = [1,2,2,1,-1,-2,-2,-1]
        used[sy][sx] = 1
        while q:
            now = q.popleft()
            y,x = now[0],now[1]
            if y == ey and x == ex:
                return used[y][x] - 1
            for i in range(8):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < L and 0 <= dx < L:
                    if used[dy][dx] == 0:
                        used[dy][dx] = used[y][x] + 1
                        q.append((dy,dx))
    ans = bfs(sy,sx,ey,ex)
    print(ans)