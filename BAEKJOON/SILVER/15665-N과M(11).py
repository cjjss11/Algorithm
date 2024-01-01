N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = [0]*M
used = [0]*N
s = set()
def abc(level):
    if level == M:
        result = " ".join(map(str,path))
        if result not in s:
            s.add(result)
            print(result)
        return
    for i in range(N):
        path[level] = lst[i]
        abc(level+1)
abc(0)