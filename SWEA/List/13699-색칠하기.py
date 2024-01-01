T = int(input())
for test_case in range(1, T + 1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input()) 
    lst = [list(map(int,input().split())) for _ in range(N)]
    def color(a):
        cnt = 0
        for i in range(lst[a][0],lst[a][2]+1):
            for j in range(lst[a][1],lst[a][3]+1):
                arr[i][j] += lst[a][-1]
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 3:
                    cnt += 1
        return cnt
 
    for i in range(N):
        result = color(i)
    print(f'#{test_case} {result}')