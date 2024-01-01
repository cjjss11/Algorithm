# 1. 인접 행렬
from collections import deque
N,M,V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
lst = []
for i in range(N+1):
    lst.append(i)
for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
used = [0]*(N+1)
path = []
def dfs(now):
    path.append(lst[now])
    if now == len(lst):
        return
    for i in range(N+1):
        if arr[now][i] == 1:
            if used[i] == 0:
                used[i] = 1
                dfs(i)
used[V] = 1
dfs(V)
print(*path)

result = []
visit = [0]*(N+1)
def bfs(st):
    q = deque()
    q.append(st)
    while q:
        now = q.popleft()
        result.append(lst[now])
        for i in range(N+1):
            if arr[now][i] == 1:
                if visit[i] == 0:
                    visit[i] = 1
                    q.append(i)
visit[V] = 1
bfs(V)
print(*result)

# 2. 인접 리스트
from collections import deque
N,M,V = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,N+1):
    arr[i].sort() # 인접 리스트로 할 경우 정렬 !
dfs_lst = []
used = [0]*(N+1)
def dfs(V):
    dfs_lst.append(V)
    for i in arr[V]:
        if used[i] == 0:
            used[i] = 1
            dfs(i)
used[V] = 1
dfs(V)

bfs_lst = []
used = [0]*(N+1)
def bfs(V):
    q = deque()
    q.append(V)
    while q:
        now = q.popleft()
        bfs_lst.append(now)
        for i in arr[now]: # now에서 갈 수 있는 경로가 now인덱스 리스트에 존재
            if used[i] == 0:
                used[i] = 1
                q.append(i)
used[V] = 1
bfs(V)
print(*dfs_lst)
print(*bfs_lst)