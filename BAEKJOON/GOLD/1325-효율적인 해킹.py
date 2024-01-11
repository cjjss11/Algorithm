from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    # a가 b를 신뢰하는 경우는 b를 해킹할 시 a도 해킹된다고 하였으므로
    arr[b].append(a)

def bfs(now):
    q = deque()
    q.append(now)
    used[now] = 1
    cnt = 1
    while q:
        now = q.popleft()
        for i in arr[now]:
            if used[i] == 0:
                used[i] = 1
                cnt += 1
                q.append(i)
    return cnt

result = [0]*(N+1)
for i in range(1,N+1):
    used = [0]*(N+1)
    cnt = bfs(i)
    result[i] = cnt
for i in range(1,N+1):
    if result[i] == max(result):
        print(i,end=" ")