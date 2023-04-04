T = 10
for test_case in range(1, T + 1):
    T1 = int(input())
    lst = [list(map(int,input().split())) for _ in range(100)]
    arr = []
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += lst[i][j]
        arr.append(row_sum)
    for i in range(100):
        column_sum = 0
        for j in range(100):
            column_sum += lst[j][i]
        arr.append(column_sum)
    cross1_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                cross1_sum += lst[i][j]
    arr.append(cross1_sum)
    cross2_sum = 0
    for i in range(100):
        for j in range(99,-1,-1):
            if i + j == 99:
                cross2_sum += lst[i][j]
    arr.append(cross2_sum)
    maxvalue = arr[0]
    for i in arr:
        if i > maxvalue:
            maxvalue = i
    print(f'#{test_case} {maxvalue}')