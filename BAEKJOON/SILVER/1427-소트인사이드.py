lst = list(map(int,input()))
result = sorted(lst, key=lambda x:x, reverse=True)
for i in result:
    print(i,end='')