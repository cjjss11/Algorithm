import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y,x):
    if dp[y][x] == 1:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        dy = y + direct_i[i]
        dx = x + direct_j[i]
        if 0 <= dy < N and 0 <= dx < N:
            if arr[y][x] < arr[dy][dx]:
                dp[y][x] = max(dp[y][x], dfs(dy,dx)+1)
    return dp[y][x]

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
dp = [[0]*N for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(answer,dfs(i,j))
print(answer)