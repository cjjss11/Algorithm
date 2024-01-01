T = int(input())
for test_case in range(1, T + 1):
    st = ''
    N = int(input())
    for i in range(N):
        a,num = input().split()
        num = int(num)
        st += a*num
    print(f'#{test_case}')
    for i in range(0,len(st),10):
            print(st[i:i+10])