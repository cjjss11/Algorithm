from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int,input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a,b = map(int,input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    S,G = map(int,input().split())

    flag = 0
    def bfs(S):
        global flag
        q = deque()
        q.append(S)
        used = [0]*(V+1)
        used[S] = 1
        while q:
            now = q.popleft()
            if now == G:
                flag = 1
                return used[G]-1

            for i in range(1,V+1):
                if arr[now][i] == 1:
                    if used[i] == 0:
                        used[i] += used[now] + 1
                        q.append(i)
    ans = bfs(S)
    if flag:
        print(f'#{test_case} {ans}')
    else:
        print(f'#{test_case} {0}')