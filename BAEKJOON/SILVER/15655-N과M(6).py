N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = [0]*M
used = [0]*N
def abc(level,start):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(start,N):
        if used[i] == 0:
            path[level] = lst[i]
            used[i] = 1
            abc(level+1,i+1)
            used[i] = 0
abc(0,0)