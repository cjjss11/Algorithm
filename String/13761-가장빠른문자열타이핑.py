T = int(input())
for test_case in range(1, T + 1):
    A,B = input().split()
    def check(a):
        for i in range(len(B)):
            if A[i+a] != B[i]:
                return 0
        return 1
    count1 = 0
    count2 = 0
    for i in range(len(A)-len(B)+1):
        result = check(i)
        if result != 0:
            count1 += 1
    st = A.replace(B,'')
    for i in st:
        count2 += 1
    print(f'#{test_case} {count1+count2}')
