R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
used = [0] * 200
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
for i in range(R):
    for j in range(C):
        arr[i][j] = ord(arr[i][j])
maxvalue = -21e8
cnt = 1
def dfs(y,x):
    global maxvalue,cnt
    if cnt > maxvalue:
        maxvalue = cnt
    for i in range(4):
        dy = y + direct_i[i]
        dx = x + direct_j[i]
        if 0 <= dy < R and 0 <= dx < C:
            if used[arr[dy][dx]] == 0:
                used[arr[dy][dx]] = 1
                cnt += 1
                dfs(dy,dx)
                used[arr[dy][dx]] = 0
                cnt -= 1

used[arr[0][0]] = 1
dfs(0,0)
print(maxvalue)
