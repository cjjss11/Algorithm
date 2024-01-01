N,M = map(int,input().split())
path = [0]*M
def abc(level,start):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(start,N):
        path[level] = i+1
        abc(level+1,i)
        path[level] = 0
abc(0,0)