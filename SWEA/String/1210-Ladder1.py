for test_case in range(1, 11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    direct_i = [0,0,-1]
    direct_j = [-1,1,0]
    used = [[0]*100 for _ in range(100)]
    answer = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                y = i
                x = j
    used[y][x] = 1
    while 1:
        if y == 0:
            answer = x
            break
        for i in range(3):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < 100 and 0 <= dx < 100:
                if arr[dy][dx] == 1:
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        y = dy
                        x = dx
                        break
    print(f'#{T} {answer}')