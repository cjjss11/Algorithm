for test_case in range(1,11):
    T = int(input())
    a,b = map(int,input().split())
    lst = [a]*b
    def abc(num,gop):
        if num == len(lst)-1:
            print(f'#{test_case} {gop}')
            return
        abc(num+1,gop*lst[num+1])

    abc(0,lst[0])