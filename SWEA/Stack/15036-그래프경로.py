T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    used = [0]*(V+1)
    for _ in range(E):
        a,b = map(int,input().split())
        arr[a][b] = 1
    S,G = map(int,input().split())
    result = 0
    def dfs(now):
        global result
        if now == G:
            result = 1
            return
        for i in range(V+1):
            if arr[now][i] == 1:
                if used[i] == 0:
                    used[i] = 1
                    dfs(i)
    used[S] = 1
    dfs(S)
    if result == 1:
        answer = 1
    else:
        answer = 0
    print(f'#{test_case} {answer}')