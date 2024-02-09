def solution(N, number):
    answer = -1
    dp = []

    # i = N의 개수
    for i in range(1, 9):
        lst = set()
        # {N}, {NN}, {NNN}...
        check = int(str(N)*i)
        lst.add(check)

        # j개를 사용해서 만든 값들
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    lst.add(x-y)
                    lst.add(x+y)
                    lst.add(x*y)
                    if y != 0:
                        lst.add(x//y)
        if number in lst:
            answer = i
            break

        dp.append(lst)
    return answer