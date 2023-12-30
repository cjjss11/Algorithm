# 첫 번째 방법
from collections import deque
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
        now = q.popleft()
        now_y,now_x = now[0],now[1]
        for i in range(4):
            dy = now_y + direct_i[i]
            dx = now_x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] > 0:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        q.append([dy,dx])

def bingha(y,x): # 높이 낮추는 함수
    cnt = 0
    for i in range(4):
        dy = y + direct_i[i]
        dx = x + direct_j[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] == 0:
                cnt += 1 # 주변 0의 개수 
    return [y,x,cnt] # 해당 좌표랑 그 좌표 주변 0의 개수 리턴

year = 0
answer = 0
while 1:
    used = [[0]*M for _ in range(N)]
    ice = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                if used[i][j] == 0:
                    used[i][j] = 1
                    bfs(i,j)
                    ice += 1
    if ice >= 2:
        answer = year
        break
    elif ice == 0:
        answer = 0
        break
    result = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                result.append(bingha(i,j)) # 리턴한 해당 좌표랑 주변 0의 개수들로 2차원 리스트
    for y,x,cnt in result:
        arr[y][x] -= cnt # 0의 개수만큼 빼주기 (높이 낮추기)
        if arr[y][x] < 0: # 0 개수만큼 다 빼주고 음수인지 확인하기
            arr[y][x] = 0 # 음수인 부분은 바다(0)으로 바꿔주는 것은 다 녹이고 난 후에 해야함
    year += 1 # 높이 다 낮춰줬으면 연도 + 1
print(answer)


# 두 번째 방법
from collections import deque
import sys
readline = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]

# 빙하 녹이는 함수
def bfs_melting():
    q = deque()
    used_melting = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and used_melting[i][j] == 0:
                used_melting[i][j] = 1
                q.append((i,j))

    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0 and used_melting[dy][dx] == 0:
                    if arr[y][x] > 0:
                        arr[y][x] -= 1

# 빙하 덩어리 개수 구하는 함수
def bfs_cnt(y,x):
    cnt_q = deque()
    cnt_q.append((y,x))
    while cnt_q:
        y,x = cnt_q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] != 0 and used_cnt[dy][dx] == 0:
                    used_cnt[dy][dx] = 1
                    cnt_q.append((dy,dx))

year = 0
while 1:
    bfs_melting()
    used_cnt = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and used_cnt[i][j] == 0:
                used_cnt[i][j] = 1
                bfs_cnt(i,j)
                cnt += 1
    year += 1
    zero = 0
    if cnt > 1:
        break
    # zero = sum(row.count(0) for row in arr) 이런 식으로도 할 수 있음
    for i in range(N):
        zero += arr[i].count(0)
    if zero == N*M:
        year = 0
        break

print(year)