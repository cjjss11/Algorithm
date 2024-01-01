N,M = map(int,input().split())
path = [0]*M
def abc(level):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        path[level] = i
        abc(level+1)
abc(0)
