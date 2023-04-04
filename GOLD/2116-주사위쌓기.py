N = int(input())
dice = [list(map(int,input().split())) for _ in range(N)]
max_lst = []
for i in range(6):
    start = i
    result = 0
    for j in range(len(dice)):
        if start == 0 or start == 5: # 만약 주사위의 인덱스가 0이나 5라면
            result += max(dice[j][1:5]) # 0,5번을 제외한 나머지 주사위 면 중 가장 큰 값을 더해줌
            if j != len(dice)-1 and start == 0: # 만약 인덱스가 마지막이 아니고 0이라면
                start = dice[j+1].index(dice[j][5]) # 다음 인덱스 값을 현재 5번째 인덱스가 존재하는 값을 다음 주사위에서 찾아서 대입
            elif j != len(dice)-1 and start == 5:
                start = dice[j+1].index(dice[j][0])

        elif start == 2 or start == 4:
            result += max(dice[j][0:2] + [dice[j][3]] + [dice[j][5]])
            if j != len(dice)-1 and start == 2:
                start = dice[j+1].index(dice[j][4])
            elif j != len(dice)-1 and start == 4:
                start = dice[j+1].index(dice[j][2])

        elif start == 1 or start == 3:
            result += max([dice[j][0]] + [dice[j][2]] + dice[j][4:])
            if j != len(dice)-1 and start == 1:
                start = dice[j+1].index(dice[j][3])
            elif j != len(dice)-1 and start == 3:
                start = dice[j+1].index(dice[j][1])
    max_lst.append(result)
print(max(max_lst))