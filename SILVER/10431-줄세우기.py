T = int(input())
for _ in range(T):
    cnt = 0
    lst = list(map(int,input().split()))
    for i in range(2,21):
        for j in range(1,i):
            if lst[i] < lst[j]:
                cnt += 1
    print(lst[0],end=' ')
    print(cnt)
