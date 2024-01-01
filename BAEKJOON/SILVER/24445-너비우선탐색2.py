import sys
from collections import deque
input = sys.stdin.readline

N,M,R = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for lst in arr:
    lst.sort(reverse=True)

used = [0]*(N+1)
used[R] = 1

result = [0]*(N+1)
result[R] = 1
idx = 1

q = deque()
q.append(R)

while q:
    now = q.popleft()
    for i in arr[now]:
        if used[i] == 0:
            idx += 1
            result[i] = idx
            used[i] = 1
            q.append(i)
for i in result[1:]:
    print(i)