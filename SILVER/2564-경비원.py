width,height = map(int,input().split())
N = int(input())
length = width*2 + height*2
result = []
for i in range(N+1):
    dir,loc = map(int,input().split())
    answer = 0
    if dir == 1:
        answer = height*2 + width + (width-loc)
        result.append(answer)
    elif dir == 2:
        answer = height + loc
        result.append(answer)
    elif dir == 3:
        answer = loc
        result.append(answer)
    elif dir == 4:
        answer = height + width + (height-loc)
        result.append(answer)
sum = 0
for i in range(len(result)-1):
    if result[i] > result[-1]:
        clock = result[-1] + length - result[i]
        r_clock = result[i] - result[-1]
        if clock > r_clock:
            sum += r_clock
        else:
            sum += clock
    elif result[i] < result[-1]:
        clock = result[-1] - result[i]
        r_clock = result[i] + length - result[-1]
        if clock > r_clock:
            sum += r_clock
        else:
            sum += clock
print(sum)