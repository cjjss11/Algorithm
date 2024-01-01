# 1. 첫번째 풀이
N,M = map(int,input().split())
card = list(map(int,input().split()))
maxvalue = -21e8
for i in range(N-2):
    for j in range(i+1,N-1):
        sum = 0
        for k in range(j+1,N):
            if card[i] + card[j] + card[k] <= M:
                sum = card[i] + card[j] + card[k]
                if sum > maxvalue:
                    maxvalue = sum
            else:
                continue
print(maxvalue)

# 2. 두번째 풀이
N,M = map(int,input().split())
card = list(map(int,input().split()))
sum = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if sum < card[i]+card[j]+card[k] <= M:
                sum = card[i]+card[j]+card[k]
print(sum)