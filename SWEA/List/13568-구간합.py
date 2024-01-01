T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    def getsum(a):
        sum = 0
        for i in range(M):
            sum += lst[i+a]
        return sum
    maxvalue = -21e8
    minvalue = 21e8
    for i in range(N-M+1):
        result = getsum(i)
        if result > maxvalue:
            maxvalue = result
        if result < minvalue:
            minvalue = result
    print(f'#{test_case} {maxvalue-minvalue}')