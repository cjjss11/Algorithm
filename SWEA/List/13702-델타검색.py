T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    direct_i = [-1,1,0,0]
    direct_j = [0,0,-1,1]
    def minus(a,b):
        sum = 0
        for i in range(4):
            di = a + direct_i[i]
            dj = b + direct_j[i]
            if 0 <= di < N and 0 <= dj < N:
                sum += abs(lst[di][dj]-lst[a][b])
        return sum
    sum1 = 0
    for i in range(N):
        for j in range(N):
            result = minus(i,j)
            sum1 += result
    print(f'#{test_case} {sum1}')