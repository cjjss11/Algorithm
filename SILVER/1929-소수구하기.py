M,N = map(int,input().split())
lst = [1]*(N+1)
lst[0] = 0
lst[1] = 0
for i in range(2,int(N**0.5)+1): # 제곱근을 사용해서 해당 제곱근 값으로 범위지정
    if lst[i] == 1:
        for j in range(i*2, N+1, i):
            lst[j] = 0
for i in range(M,N+1):
    if lst[i] == 1:
        print(i)