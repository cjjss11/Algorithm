import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    answer = 0
    used = [0]*n
    def dfs(now):
        for i in range(n):
            if now != i and computers[now][i] == 1:
                if used[i] == 0:
                    used[i]= 1
                    dfs(i)
    for i in range(n):
        if used[i] == 0:
            dfs(i)
            answer += 1
    return answer