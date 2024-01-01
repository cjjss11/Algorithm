N = int(input())
lst = list(map(int,input().split()))
op = list(map(int,input().split()))
maxvalue = -21e8
minvalue = 21e8

def dfs(plus,minus,multiply,divide,level,value):
    global maxvalue,minvalue
    if level == N:
        if value < minvalue:
            minvalue = value
        if value > maxvalue:
            maxvalue = value
        return

    if plus > 0:
        dfs(plus-1,minus,multiply,divide,level+1,value+lst[level])
    if minus > 0:
        dfs(plus,minus-1,multiply,divide,level+1,value-lst[level])
    if multiply > 0:
        dfs(plus,minus,multiply-1,divide,level+1,value*lst[level])
    if divide > 0:
        dfs(plus,minus,multiply,divide-1,level+1,int(value/lst[level]))

dfs(op[0],op[1],op[2],op[3],1,lst[0])
print(maxvalue)
print(minvalue)