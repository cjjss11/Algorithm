# 첫 번째 방법

N,M = map(int,input().split())
lst = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)

used = [0]*N
flag = 0
def dfs(now,level):
    global flag
    # level이 1부터 시작했으므로 5
    if level == 5:
        flag = 1
        return

    for i in lst[now]:
        if used[i] == 0:
            used[i] = 1
            dfs(i,level+1)
            used[i] = 0

for i in range(N):
    used[i] = 1
    dfs(i,1)
    used[i] = 0

    if flag == 1:
        break
print(flag)

# 두 번째 방법

N, M = map(int, input().split())
lst = [[] for _ in range(N)]  # 친구 관계 인접리스트

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

flag = 0
used = [0]*N
def dfs(now, level):
    global flag
    if level == 5:
        flag = 1
        return
    else:
        used[now] = 1
        for i in lst[now]:
            if used[i] == 0:
                dfs(i, level+1)
        used[now] = 0

for i in range(N):
    dfs(i, 1)
    if flag == 1:  # 없으면 시간 초과
        break

print(flag)