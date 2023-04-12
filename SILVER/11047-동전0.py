N,K = map(int,input().split())
lst = []
for _ in range(N):
    a = int(input())
    lst.append(a)
coin = sorted(lst, key=lambda x:x, reverse=True)
cnt = 0
for i in coin:
    if K >= i:
        cnt += K // i
        K -= i * (K//i)
print(cnt,end='')