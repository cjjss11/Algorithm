N,M = map(int,input().split())
path = [0]*M
used = [0]*(N+1)
def abc(level):
    if level == M:
        if M > 1:
            for i in range(M-1): # 오름차순 정렬인지 검사
                if path[i] > path[i+1]: # 오름차순이 아니면 return
                    return
            for i in range(M): # 오름차순이 맞으면 출력
                print(path[i],end=' ')
            print()
        else:
            for i in range(M):
                print(path[i],end=' ')
            print()
        return
    for i in range(1,N+1):
        if used[i] == 0:
            path[level] = i
            used[i] = 1
            abc(level+1)
            used[i] = 0
abc(0)