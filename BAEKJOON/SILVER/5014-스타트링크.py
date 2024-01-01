from collections import deque
F,S,G,U,D = map(int,input().split())
flag = 0
def bfs(S):
    global flag
    q = deque()
    q.append(S)
    used = [0]*(F+1)
    used[S] = 1
    direct = [U,-D] # 위 아래로만 갈 수 있음
    while q:
        now = q.popleft()
        if now == G:
            flag = 1
            return used[G]-1
        for i in range(2):
            EV = now + direct[i]
            if 0 < EV <= F:
                if used[EV] == 0:
                    used[EV] = used[now] + 1
                    q.append(EV)
ans = bfs(S)
if flag:
    print(ans)
else:
    print('use the stairs')