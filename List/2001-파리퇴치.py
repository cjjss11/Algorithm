T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    def getsum(a,b):
        sum = 0
        for i in range(M):
            for j in range(M):
                sum += arr[i+a][j+b]
        return sum
    maxvalue = -21e8
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = getsum(i,j)
            if result > maxvalue:
                maxvalue = result
    print(f'#{test_case} {maxvalue}')