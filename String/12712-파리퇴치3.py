T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    def getsum1(a,b):
        sum1 = 0
        direct_i = [-1,1,0,0]
        direct_j = [0,0,-1,1]
        for i in range(4):
            for j in range(1,M):
                di = a + direct_i[i] * j
                dj = b + direct_j[i] * j
                if 0 <= di < N and 0 <= dj < N:
                    sum1 += arr[di][dj]
        sum1 = sum1 + arr[a][b]
        return sum1
    def getsum2(a,b):
        sum2 = 0
        cross_i = [-1,-1,1,1]
        cross_j = [-1,1,-1,1]
        for i in range(4):
            for j in range(1,M):
                di = a + cross_i[i] * j
                dj = b + cross_j[i] * j
                if 0 <= di < N and 0 <= dj < N:
                    sum2 += arr[di][dj]
        sum2 = sum2 + arr[a][b]
        return sum2
 
    maxvalue1 = -21e8
    maxvalue2 = -21e8
    for i in range(N):
        for j in range(N):
            result1 = getsum1(i,j)
            result2 = getsum2(i,j)
            if result1 > maxvalue1:
                maxvalue1 = result1
            if result2 > maxvalue2:
                maxvalue2 = result2
 
    if maxvalue1 > maxvalue2:
        print(f'#{test_case} {maxvalue1}')
    elif maxvalue1 < maxvalue2:
        print(f'#{test_case} {maxvalue2}')