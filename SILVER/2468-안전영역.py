from collections import deque
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
minvalue = 21e8 # 높이 최솟값
maxvalue = -21e8 # 높이 최대값
for i in range(N):
    for j in range(N):
        if arr[i][j] > maxvalue:
            maxvalue = arr[i][j]
        if arr[i][j] < minvalue:
            minvalue = arr[i][j]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    while q:
        now = q.popleft()
        now_y,now_x = now[0],now[1]
        for i in range(4):
            dy = now_y + direct_i[i]
            dx = now_x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] > n:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        q.append([dy,dx])
max_lst = []
maxvalue1 = 1 # 아무 지역도 물에 잠기지 않을 때 1
for n in range(minvalue, maxvalue): # 안전 영역 최대 개수 찾기
    used = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > n:
                if used[i][j] == 0:
                    used[i][j] = 1
                    bfs(i,j)
                    cnt += 1

    if cnt > maxvalue1:
        maxvalue1 = cnt
print(maxvalue1)
