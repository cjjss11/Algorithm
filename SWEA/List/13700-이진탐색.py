T = int(input())
for test_case in range(1, T + 1):
    P, A, B = map(int,input().split())
    left = 1
    right = P
    def binary_search_A(left,right,target):
        cnt = 0
        while 1:
            c = int((left + right) // 2)
            if target != c:
                if c > target:
                    right = c
                if c < target:
                    left = c
            if target == c:
                break
            cnt += 1
        return cnt
 
    answerA = binary_search_A(left,P,A)
    def binary_search_B(left,right,target):
        cnt = 0
        while 1:
            c = int((left + right) // 2)
            if target != c:
                if c > target:
                    right = c
                if c < target:
                    left = c
            if target == c:
                break
            cnt += 1
        return cnt
    answerB = binary_search_B(left,P,B)
    if answerA > answerB:
        print(f'#{test_case} B')
    elif answerA < answerB:
        print(f'#{test_case} A')
    elif answerA == answerB:
        print(f'#{test_case} 0')