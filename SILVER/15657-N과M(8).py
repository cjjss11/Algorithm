N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = [0]*M
def abc(level,start):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(start,N):
        path[level] = lst[i]
        abc(level+1,i)
abc(0,0)