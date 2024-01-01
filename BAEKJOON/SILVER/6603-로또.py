while 1:
    K,*lotto = map(int,input().split())
    if K == 0:
        break
    lotto.sort()
    path = [0]*6
    used = [0]*K
    def abc(level,start):
        if level == 6:
            for i in range(6):
                print(path[i],end=' ')
            print()
            return
        for i in range(start,K):
            if used[i] == 0:
                path[level] = lotto[i]
                used[i] = 1
                abc(level+1,i+1)
                used[i] =0
    abc(0,0)
    print()