from collections import deque
while 1:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break

    arr = []
    for _ in range(L):
        lst = []
        for _ in range(R):
            row = input().strip()
            lst.append(row)
        input()
        arr.append(lst)

    direct_i = [-1,1,0,0,0,0]
    direct_j = [0,0,-1,0,1,0]
    direct_k = [0,0,0,1,0,-1]
    def bfs(y,x,z):
        q = deque()
        q.append([y,x,z])
        used = [[[0]*C for _ in range(R)] for _ in range(L)]
        used[y][x][z] = 1
        while q:
            now = q.popleft()
            y,x,z = now[0],now[1],now[2]
            if arr[y][x][z] == 'E':
                return f'Escaped in {used[y][x][z] - 1} minute(s).'
            for i in range(6):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                dz = z + direct_k[i]
                if 0 <= dy < L and 0 <= dx < R and 0 <= dz < C:
                    if arr[dy][dx][dz] != '#':
                        if used[dy][dx][dz] == 0:
                            used[dy][dx][dz] = used[y][x][z] + 1
                            q.append([dy,dx,dz])
        return f'Trapped!'
    
    ans = 'Trapped!'
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    ans = bfs(i,j,k)
    print(ans)