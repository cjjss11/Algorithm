T = int(input())
for test_case in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    def row():
        for i in range(9):
            lst = []
            for j in range(9):
                if arr[i][j] not in lst:
                    lst.append(arr[i][j])
                else:
                    return 0
        return 1
    def column():
        for i in range(9):
            lst = []
            for j in range(9):
                if arr[j][i] not in lst:
                    lst.append(arr[j][i])
                else:
                    return 0
        return 1
    def check():
        for i in range(0,9,3):
            for j in range(0,9,3):
                lst = []
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        if arr[m][n] not in lst:
                            lst.append(arr[m][n])
                        else:
                            return 0
        return 1
    result1 = row()
    result2 = column()
    result3 = check()
    if result1 != 0 and result2 != 0 and result3 != 0:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')