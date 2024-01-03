import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])

def dfs(now,dist):
    for a,b in arr[now]:
        if used[a] == -1:
            used[a] = dist + b
            dfs(a,dist+b)

used = [-1]*(n+1)
used[1] = 0
dfs(1,0)
idx,maxx = 0,0
# 최댓값과 그 최댓값의 인덱스를 구하는 코드인데
# used.index(max(used)) 이런 식으로 간단하게 할 수 있
for i in range(1,len(used)):
    if used[i] > maxx:
        maxx = used[i]
        idx = i
used = [-1]*(n+1)
# 1에서 가장 먼 곳에서 다시 먼 곳을 찾기
used[idx] = 0
dfs(idx,0)
print(max(used))