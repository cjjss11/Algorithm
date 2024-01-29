from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]

def bfs():
    q = deque()
    q.append((0,0))
    used = [[0] * M for _ in range(N)]
    cnt = 0
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < N and 0 <= dx < M:
                if arr[dy][dx] == 0 and used[dy][dx] == 0:
                    used[dy][dx] = 1
                    q.append((dy,dx))
                # (0,0)에서 시작해서 처음 만나는 1들은 모두 가장자리
                elif arr[dy][dx] == 1:
                    # 따로 리스트 만들어 추가하고 한 번에 0으로 바꿔줄 수도 있지만
                    # 여기서는 추가하지 않고 바로 0으로 바꿔주어 녹게 만들어줌
                    arr[dy][dx] = 0
                    used[dy][dx] = 1
                    # 녹은 치즈 개수
                    cnt += 1
    return cnt

result = []
time = 0
while 1:
    ans = bfs()
    result.append(ans)
    # 녹은 치즈가 0이라는 것은 이미 모두 다 녹아서 없다는 의미
    if ans == 0:
        break
    time += 1
# 한 시간 전에(모두 녹기 전 단계) cnt를 출력해야 되므로 [-2] 출력
print(result[-2])