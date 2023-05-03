from collections import deque
N,M,K,X = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)
for lst in arr:
    lst.sort()
used = [0]*(N+1)
def bfs(X):
    q = deque()
    q.append(X)
    used[X] = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if used[i] == 0:
                used[i] = used[now] + 1
                q.append(i)
bfs(X)
flag = 0
for i in range(len(used)):
    if used[i]-1 == K: # 최단 거리가 K인 경우
        flag = 1
        print(i)
if flag == 0:
    print(-1)