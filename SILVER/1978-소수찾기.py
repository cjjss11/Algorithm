N = int(input())
lst = list(map(int,input().split()))
cnt_lst = []
for i in range(len(lst)):
    cnt = 0
    for j in range(2,lst[i]+1):
        if lst[i] == 1:
            continue
        if lst[i] % j == 0:
            cnt += 1
    if cnt == 1:
        cnt_lst.append(cnt)

print(len(cnt_lst))