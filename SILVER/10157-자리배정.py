C,R = map(int,input().split())
K = int(input())
if C*R < K:
    print(0)
else:
    # 주변을 1로 둘러쌈
    arr = [[1] * (C + 2)] + [[1] + [0] * C + [1] for _ in range(R)] + [[1] * (C + 2)]
    direct_i = [1,0,-1,0]
    direct_j = [0,1,0,-1]
    y,x = 1,1
    dr = 0
    for i in range(1,K):
        arr[y][x] = i
        dy = y + direct_i[dr]
        dx = x + direct_j[dr]
        if arr[dy][dx] == 0:
            y,x = dy,dx
        else:
            dr = (dr+1) % 4 # 방향 꺾기
            y = y + direct_i[dr]
            x = x + direct_j[dr]
    print(f'{x} {y}')