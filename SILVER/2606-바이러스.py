computer = int(input())
N = int(input())
lst = []
arr = [[0]*(computer+1) for _ in range(computer+1)]
for i in range(computer+1):
    lst.append(i)
for _ in range(N):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
used = [0]*(computer+1)
cnt = 0
def dfs(now):
    global cnt
    if now == len(lst):
        return
    for j in range(len(lst)):
        if arr[now][j] == 1:
            if used[j] == 0:
                used[j] = 1
                cnt += 1
                dfs(j)
used[1] = 1
dfs(1)
print(cnt)