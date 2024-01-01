N = int(input())
lst = list(map(int,input().split()))
maxvalue = -21e8
minvalue = 21e8
for i in range(len(lst)):
    if lst[i] > maxvalue:
        maxvalue = lst[i]
    if lst[i] < minvalue:
        minvalue = lst[i]
print(f'{minvalue} {maxvalue}')