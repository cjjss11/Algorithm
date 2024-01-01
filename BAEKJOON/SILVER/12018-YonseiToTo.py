N,M = map(int,input().split())
lst = []
for i in range(N):
    P,L = map(int,input().split())
    coin = list(map(int,input().split()))
    coin.sort(reverse=True)

    if P < L: # 신청인원이 수강 가능한 인원보다 작은 경우
        lst.append(1) # 최소 1
    else:
        # 수강 가능한 인원 중 마지막 인원의 마일리지
        lst.append(coin[L-1])
lst.sort()

cnt = 0
for i in range(len(lst)):
    if M >= lst[i]:
        M -= lst[i]
        cnt += 1
print(cnt)
