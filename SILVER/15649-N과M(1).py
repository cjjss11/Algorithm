N,M = map(int,input().split())
path = [0]*M
used = [0]*(N+1)
def abc(level):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(1,N+1):
        if used[i] == 0:
            used[i] = 1
            path[level] = i
            abc(level+1)
            used[i] = 0
abc(0)