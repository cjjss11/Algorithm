T = int(input())
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split())
    charge_lst = list(map(int,input().split()))
    current = 0
    count = 0
    while current + K < N:
        for i in range(K,0,-1):
            if (current+i) in charge_lst:
                current += i
                count += 1
                break
        else:
            count = 0
            break
    print(f'#{test_case} {count}')