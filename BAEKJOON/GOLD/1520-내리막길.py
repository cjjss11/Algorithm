import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
direct_i = [-1,0,1,0]
direct_j = [0,1,0,-1]
def dfs(y,x):
    if y == N-1 and x == M-1:
        return 1

    # 이미 dp[y][x]에 값이 저장되어 있다면 해당 값을 반환
    # 이는 중복 계산을 피하기 위하 부분
    if dp[y][x] != -1:
        return dp[y][x]

    # 초기에 dp[y][x]를 0으로 설정한 후 상하좌우로 이동하면서 
    # 현재 위치의 높이보다 낮은 지점으로만 이동
    dp[y][x] = 0
    
    for i in range(4):
        dy = y + direct_i[i]
        dx = x + direct_j[i]
        if 0 <= dy < N and 0 <= dx < M:
            if arr[dy][dx] < arr[y][x]:
                dp[y][x] += dfs(dy,dx)
    return dp[y][x]

print(dfs(0,0))