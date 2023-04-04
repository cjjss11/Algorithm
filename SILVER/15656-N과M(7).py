N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = [0]*M
def abc(level):
    if level == M:
        for i in range(M):
            print(path[i],end=' ')
        print()
        return
    for i in range(N):
        path[level] = lst[i]
        abc(level+1)

abc(0)