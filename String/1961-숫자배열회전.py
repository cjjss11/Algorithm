T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    lst_90 = []
    lst_180 = []
    lst_270 = []
    for j in range(N): # 90도
        lst = []
        for i in range(N-1,-1,-1):
            lst.append(arr[i][j])
        lst_90.append(lst)
 
    for i in range(N-1,-1,-1): # 180도
        lst = []
        for j in range(N-1,-1,-1):
            lst.append(arr[i][j])
        lst_180.append(lst)
 
    for j in range(N-1,-1,-1): # 270도
        lst = []
        for i in range(N):
            lst.append(arr[i][j])
        lst_270.append(lst)
 
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(lst_90[i][j],end='')
        print(end=' ')
        for j in range(N):
            print(lst_180[i][j],end='')
        print(end=' ')
        for j in range(N):
            print(lst_270[i][j],end='')
        print()