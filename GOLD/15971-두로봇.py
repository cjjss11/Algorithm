from collections import deque

N,A,B = map(int,input().split())

lst = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))
    lst[b].append((a,c))

def bfs():
    q = deque()
    q.append([A,0,0])
    used = [0]*(N+1)
    used[A] = 1

    while q:
        now,total,max_cost = q.popleft()
        if now == B:
            return total - max_cost
        for nxt,cost in lst[now]:
            if used[nxt] == 0:
                used[nxt] = 1
                q.append([nxt,total+cost,max(max_cost,cost)])
print(bfs())