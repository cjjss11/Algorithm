N = int(input())
lst = []
for _ in range(N):
    x,y = map(int,input().split())
    lst.append([x,y])
result = sorted(lst, key=lambda x:(x[1],x[0]))
for ans in result:
    print(*ans)