import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
used = [0]*(N+1)
answer = [0]*(N+1)

def dfs(now):
    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            answer[i] = now
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(answer[i])