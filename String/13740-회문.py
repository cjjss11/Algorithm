T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr1 = [list(input()) for _ in range(N)]
    arr2 = []
    for i in range(N):
        lst = []
        for j in range(N):
            lst.append(arr1[j][i])
        arr2.append(lst)
    def horizon(a,b):
        for j in range(M):
            if arr1[a][b+j] != arr1[a][b+M-j-1]:
                return 0
        return 1
    def vertical(a,b):
        for j in range(M):
            if arr2[a][b+j] != arr2[a][b+M-j-1]:
                return 0
        return 1
    for i in range(N):
        for j in range(N-M+1):
            result1 = horizon(i,j)
            result2 = vertical(i,j)
            if result1:
                print(f'#{test_case}', end=' ')
                for k in range(j,j+M):
                    print(arr1[i][k],end='')
                print()
            if result2:
                print(f'#{test_case}', end=' ')
                for k in range(j,j+M):
                    print(arr2[i][k],end='')
                print()