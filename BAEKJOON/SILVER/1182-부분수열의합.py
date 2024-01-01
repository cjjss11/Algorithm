N,S = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
path = []*N
sum = 0
def abc(level,start):
    global cnt,sum
    if level == N:
        return
    for i in range(start,N):
        sum += lst[i]
        if sum == S:
            cnt += 1
        abc(level+1, i+1)
        sum -= lst[i]
abc(0,0)
print(cnt)