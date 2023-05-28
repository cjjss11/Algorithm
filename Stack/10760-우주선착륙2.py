T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    direct_i = [-1,-1,-1,0,1,1,1,0]
    direct_j = [-1,0,1,1,1,0,-1,-1]
    def check(a,b):
        count1 = 0
        for i in range(8):
            di = a + direct_i[i]
            dj = b + direct_j[i]
            if 0 <= di < N and 0 <= dj < M:
                if arr[a][b] > arr[di][dj]:
                    count1 += 1
        if count1 >= 4:
            return 1
        else:
            return 0
    count2 = 0
    for i in range(N):
        for j in range(M):
            result = check(i,j)
            if result:
                count2 += 1
    print(f'#{test_case} {count2}')