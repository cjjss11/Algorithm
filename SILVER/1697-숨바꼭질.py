from collections import deque
N,K = map(int,input().split())
def bfs(N):
    q = deque()
    q.append(N)
    used = [0]*200001 # 방문 배열을 200001로 만드는게 핵심
    used[N] = 1
    while q:
        now = q.popleft()
        if now == K:
            print(used[now]-1)
        direct = [-1, 1, now]
        for i in range(3):
            X = now + direct[i]
            if 0 <= X <= 200000:
                if used[X] == 0:
                    q.append(X)
                    used[X] = used[now]+1

bfs(N)