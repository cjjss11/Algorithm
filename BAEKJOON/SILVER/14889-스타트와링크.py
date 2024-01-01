N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
used = [0]*N
minvalue = 21e8
def dfs(level,start):
    global minvalue
    if level == N//2: # 두 팀으로 나누기 위해 N을 2로 나눈 값이 되면 return
        start_team = 0
        link_team = 0
        for i in range(N):
            for j in range(N):
                if used[i] == 1 and used[j] == 1: # return 되기 전에 1 체크하고 왔기 때문에 1 체크 한 사람끼리 팀
                    start_team += arr[i][j]
                elif used[i] == 0 and used[j] == 0: # 1 체크가 안 된 사람끼리 팀
                    link_team += arr[i][j]
        if abs(start_team-link_team) < minvalue:
            minvalue = abs(start_team-link_team)
        return
    for i in range(start,N): # 조합을 이용해서 팀 구성
        if used[i] == 0:
            used[i] = 1
            dfs(level+1, i+1)
            used[i] = 0
dfs(0,0)
print(minvalue)