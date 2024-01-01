N,M = map(int,input().split())
lst = [0]*(N+1)
for _ in range(M):
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        lst[i] = c
for i in range(1,len(lst)):
    print(lst[i],end=' ')