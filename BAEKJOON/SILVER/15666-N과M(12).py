N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
path = [0]*M
answer = []
def abc(level,start):
    if level == M:
        result = " ".join(map(str,path))
        if result not in answer:
            answer.append(result)
        return
    for i in range(start,N):
        path[level] = lst[i]
        abc(level+1, i)
abc(0,0)
for i in answer:
    print(i)