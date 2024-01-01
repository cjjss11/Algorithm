T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    def check(a):
        for i in range(len(str1)):
            if str2[i+a] != str1[i]:
                return 0
        return 1
    flag = 0
    for i in range(len(str2)-len(str1)+1):
        result = check(i)
        if result:
            flag = 1
    if flag:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')