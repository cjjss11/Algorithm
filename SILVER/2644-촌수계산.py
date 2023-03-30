# 1. DFS로 풀이
N = int(input())
x,y = map(int,input().split())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
used = [0]*(N+1)
flag = 0
cnt = 0
def dfs(now):
    global flag,cnt
    if now == y: # now는 입력받은 x
        flag = 1 # dfs 돌다가 now가 y랑 같으면 flag = 1 하고 리턴
        print(cnt)
        return
    for i in range(N+1):
        if arr[now][i] == 1:
            if used[i] == 0:
                used[i] = 1
                cnt += 1
                dfs(i)
                cnt -= 1

used[x] = 1
dfs(x)
if flag == 0:
    print(-1)

# 2. BFS로 풀이
from collections import deque
N = int(input())
x,y = map(int,input().split())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def bfs(x):
    q = deque()
    q.append(x)
    used = [0]*(N+1)
    used[x] = 1
    while q:
        now = q.popleft()
        if now == y:
            return used[now] - 1
        for i in range(N+1):
            if arr[now][i] == 1:
                if used[i] == 0:
                    used[i] += used[now] + 1
                    q.append(i)
    return -1

answer = bfs(x)
print(answer)