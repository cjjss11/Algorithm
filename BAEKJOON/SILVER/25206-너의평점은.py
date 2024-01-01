sum = 0
length = 20
score_sum = 0
for _ in range(length):
    book,score,grade = input().split()
    score = float(score)
    if grade == 'A+':
        sum += score * 4.5
        score_sum += score
    elif grade == 'A0':
        sum += score * 4.0
        score_sum += score
    elif grade == 'B+':
        sum += score * 3.5
        score_sum += score
    elif grade == 'B0':
        sum += score * 3.0
        score_sum += score
    elif grade == 'C+':
        sum += score * 2.5
        score_sum += score
    elif grade == 'C0':
        sum += score * 2.0
        score_sum += score
    elif grade == 'D+':
        sum += score * 1.5
        score_sum += score
    elif grade == 'D0':
        sum += score * 1.0
        score_sum += score
    elif grade == 'F':
        sum += score * 0.0
        score_sum += score
    elif grade == 'P':
        sum += 0
avg = sum / score_sum
print(avg)