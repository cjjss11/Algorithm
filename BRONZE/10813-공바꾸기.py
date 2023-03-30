N,M = map(int,input().split())
lst = [0]*(N+1)
for i in range(1,N+1):
    lst[i] = i
for _ in range(M):
    a,b = map(int,input().split())
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
for i in range(1,len(lst)):
    print(lst[i],end=' ')