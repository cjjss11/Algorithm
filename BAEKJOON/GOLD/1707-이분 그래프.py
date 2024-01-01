import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now, group):
    global flag
    if flag:
        return
    used[now] = group
    for i in arr[now]:
        if used[i] == 0:
            dfs(i, -group)
        elif used[now] == used[i]:
            flag = 1
            return

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    used = [0] * (V + 1)
    flag = 0
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in range(1, V + 1):
        if used[i] == 0:
            dfs(i, 1)
            if flag:
                break
    if flag:
        print('NO')
    else:
        print('YES')