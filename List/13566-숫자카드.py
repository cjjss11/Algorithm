T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int,input()))
    bucket = [0]*10
    for i in range(len(lst)):
        bucket[lst[i]] += 1
    maxvalue = -21e8
    maxi = 0
    for i in range(len(bucket)):
        if bucket[i] > maxvalue:
            maxvalue = bucket[i]
        if bucket[i] == maxvalue:
            if i > maxi:
                maxi = i
    print(f'#{test_case} {maxi} {maxvalue}')
