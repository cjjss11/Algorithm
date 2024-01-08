import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now):
    global result
    used[now] = 1
    lst.append(now)
    num = arr[now]
    if used[num] == 1:
        if num in lst:
            result += lst[lst.index(num):]
        return
    else:
        dfs(num)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    result = []
    used = [0] * (N + 1)
    for i in range(1,N+1):
        if used[i] == 0:
            lst = []
            dfs(i)

    print(N-len(result))