T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0]*N
    minvalue = 21e8
    def abc(level,sum):
        global minvalue
        if sum > minvalue:
            return
        if level == N:
            if sum < minvalue:
                minvalue = sum
            return
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                abc(level+1,sum+arr[level][i])
                used[i] = 0
    abc(0,0)
    print(f'#{test_case} {minvalue}')