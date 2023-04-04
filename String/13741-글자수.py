T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    def check(value):
        count = 0
        for i in range(len(str2)):
            if str2[i] == value:
                count += 1
        return count
    maxvalue = -21e8
    for i in range(len(str1)):
        result = check(str1[i])
        if result > maxvalue:
            maxvalue = result
    print(f'#{test_case} {maxvalue}')