from collections import deque

N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]

q = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            q.append((arr[i][j],i,j))
# 번호가 낮은 종류의 바이러스부터 먼저 증식하므로 정렬
q.sort()
q = deque(q)

cnt = 0
while q:
    if cnt == S:
        break
    # q 길이 동안 for문 돌림
    for _ in range(len(q)):
        virus,y,x = q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < N:
                if arr[dy][dx] == 0:
                    arr[dy][dx] = virus
                    q.append((virus,dy,dx))
    cnt += 1

print(arr[X-1][Y-1])
