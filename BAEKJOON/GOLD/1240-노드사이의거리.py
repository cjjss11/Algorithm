from collections import deque
N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])

lst = []
for _ in range(M):
    a,b = map(int,input().split())
    lst.append([a,b])

def bfs(start,end):
    q = deque()
    q.append([start,0])
    used[start] = 1

    while q:
        node,distance = q.popleft()
        if node == end:
            return distance
        for next, next_dist in arr[node]:
            if used[next] == 0:
                q.append([next,distance+next_dist])
                used[next] = 1

for start,end in lst:
    used = [0] * (N+1)
    result = bfs(start,end)
    print(result)
