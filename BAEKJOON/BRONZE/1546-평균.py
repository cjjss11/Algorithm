N = int(input())
score = list(map(int,input().split()))
M = -21e8
for i in range(len(score)):
    if score[i] > M:
        M = score[i]
for i in range(len(score)):
    score[i] = score[i] / M * 100
sum = 0
for i in range(len(score)):
    sum += score[i]
avg = sum / len(score)
print(avg)