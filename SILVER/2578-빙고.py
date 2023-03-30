arr = [list(map(int,input().split())) for _ in range(10)]
lst1 = [] # 철수 빙고판
lst2 = [] # 사회자가 부를 숫자
for i in range(5):
    lst11 = []
    for j in range(5):
        lst11.append(arr[i][j])
    lst1.append(lst11)
for i in range(5,10):
    for j in range(5):
        lst2.append(arr[i][j])
def Bingo(value):
    for i in range(5):
        for j in range(5):
            if lst1[i][j] == value: # 사회자가 부른 숫자와 같으면
                lst1[i][j] = 0 # 0 체크
                return 0
def bingo_check():
    bingo = 0
    for m in range(5): # 가로 체크
        h_cnt = 0
        for n in range(5):
            if lst1[m][n] == 0:
                h_cnt += 1
        if h_cnt == 5:
            bingo += 1
    for m in range(5): # 세로 체크
        v_cnt = 0
        for n in range(5):
            if lst1[n][m] == 0:
                v_cnt += 1
        if v_cnt == 5:
            bingo += 1
    c_cnt = 0
    for m in range(5):
        if lst1[m][m] == 0:
            c_cnt += 1 # 오른쪽 아래 방향 대각선
    if c_cnt == 5:
        bingo += 1
    cr_cnt = 0
    for m in range(5):
        if lst1[m][4-m] == 0:
            cr_cnt += 1 # 왼쪽 아래 방향 대각선
    if cr_cnt == 5:
        bingo += 1
    return bingo
idx = 0
for i in range(25):
    Bingo(lst2[i])
    if bingo_check() >= 3:
        idx = i+1
        break
print(idx)