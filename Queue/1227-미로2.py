from collections import deque
for test_case in range(1, 11):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(100)]
    def bfs(y,x):
        q = deque()
        q.append([y,x])
        direct_i = [-1,0,1,0]
        direct_j = [0,1,0,-1]
        while q:
            now = q.popleft()
            y,x = now[0],now[1]
            if y == ey and x == ex:
                return 1
            for i in range(4):
                dy = y + direct_i[i]
                dx = x + direct_j[i]
                if 0 <= dy < 100 and 0 <= dx < 100:
                    if arr[dy][dx] == 0:
                        if used[dy][dx] == 0:
                            used[dy][dx] = 1
                            q.append([dy,dx])

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 3: # 도착인 3을 찾고
                ey,ex = i,j # 좌표 값 저장하고
                arr[i][j] = 0 # 0으로 바꿔줌 -> q에 들어가서 도착 지점을 찾을 수 있게 하기 위해

    used = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                if used[i][j] == 0:
                    used[i][j] = 1
                    ans = bfs(i,j)
    if ans:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')