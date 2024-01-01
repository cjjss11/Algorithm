N = int(input())

def check(num):
    if num < 2:
        return 0
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def dfs(num,length):
    if length == N:
        if check(num) == 1:
            print(num)
        return
    for i in range(1,10):
        next_num = num * 10 + i
        if check(next_num):
            dfs(next_num,length+1)

dfs(0,0)