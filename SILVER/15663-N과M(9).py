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
        if used[i] == 0:
            path[level] = lst[i]
            used[i] = 1
            abc(level+1)
            used[i] = 0
abc(0)