N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
used = [0]*N
path = [0]*M
def abc(level):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(len(lst)):
        if used[i] == 0:
            path[level] = lst[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0
            path[level] = 0
abc(0)
