from collections import deque

M,N = map(int,input().split())
arr = [list(input()) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    used = [[0]*M for _ in range(N)]
    used[y][x] = 1
    while q:
        y,x = q.popleft()
        if y == N-1 and x == M-1:
            return used[y][x] - 1
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M and used[dy][dx] == 0:
                if arr[dy][dx] == '0':
                    used[dy][dx] = used[y][x]
                    # 왼쪽에 추가해서 먼저 pop 될 수 있도록 함
                    q.appendleft([dy,dx])
                else:
                    used[dy][dx] = used[y][x] + 1
                    q.append([dy,dx])

print(bfs(0,0))