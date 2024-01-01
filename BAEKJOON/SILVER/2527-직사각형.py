for _ in range(4):
    sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2 = map(int,input().split()) # 시작점,끝점
    if sy1 > ey2 or ey1 < sy2 or sx1 > ex2 or ex1 < sx2: # 바깥쪽에 있는 경우
        ans = 'd'
    elif ex1 == sx2 or sx1 == ex2:   # 세로가 일치(붙어있는 경우)
        if ey1 == sy2 or sy1 == ey2: # 가로가 일치(붙어있는 경우)
            ans = 'c'
        else:                         # 점 (가로,세로 둘 다 붙어 있는 경우)
            ans = 'b'                 # 변 (하나만 붙어 있는 경우)
    elif ey1 == sy2 or sy1 == ey2:    # 세로가 일치하지 않고 가로가 일치하는 경우
        ans = 'b'
    else:
        ans = 'a'
    print(ans)