N = int(input())
used = [0]*N
cross_used1 = [0]*(N+(N-1))
cross_used2 = [0]*(N+(N-1))
cnt = 0
def abc(level):
    global cnt
    if level == N:
        cnt += 1
        return
    for i in range(N):
        if used[i] == 0:
            if cross_used1[level+i] == 0: # level = 행, i = 열
                # i - level을 하면 음수 부분이 나오기 때문에 N-1을 해주므로써 양수로 만들어줌
                if cross_used2[(i-level)+(N-1)] == 0: 
                    used[i] = 1
                    cross_used1[level+i] = 1
                    cross_used2[(i-level)+(N-1)] = 1
                    abc(level+1)
                    used[i] = 0
                    cross_used1[level+i] = 0
                    cross_used2[(i-level)+(N-1)] = 0
abc(0)
print(cnt)