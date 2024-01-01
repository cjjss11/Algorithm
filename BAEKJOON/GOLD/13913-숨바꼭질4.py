from collections import deque
N,K = map(int,input().split())
used = [0] * 200001
move = [0] * 200001
def path(x): # 경로 찾기 위한 함수
    result = []
    temp = x
    for _ in range(used[x]+1):
        result.append(temp)
        temp = move[temp]
    result.reverse()
    print(*result[1:])

def bfs(N):
    q = deque()
    q.append(N)
    used[N] = 1
    while q:
        now = q.popleft()
        direct = [-1,1,now]
        if now == K:
            print(used[now]-1)
            path(now)
        for i in range(3):
            X = now + direct[i]
            if 0 <= X < 200001:
                if used[X] == 0:
                    used[X] = used[now] + 1
                    q.append(X)
                    move[X] = now
bfs(N)