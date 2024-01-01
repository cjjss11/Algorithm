from collections import deque
N,K = map(int,input().split())
def bfs(N):
    q = deque()
    q.append(N)
    used = [0] * 200001
    used[N] = 1
    while q:
        now = q.popleft()
        if now == K:
            return used[now]-1
        direct = [now,-1,1] # *2, -1, 1 순서대로 !!
        for i in range(3):
            move = now + direct[i]
            if 0 <= move < 200001:
                if i == 0: # 0초 후에 *2 이동한다 했으므로 조건으로 따로 계산
                    if used[move] == 0:
                        used[move] = used[now] # 0초라고 하였으니 used의 now 값과 같아야함
                        q.append(move)
                else: # 1초 후에 -1 또는 +1 이동
                    if used[move] == 0:
                        used[move] = used[now] + 1
                        q.append(move)
ans = bfs(N)
print(ans)