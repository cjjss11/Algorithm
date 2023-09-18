lst = input().split('-')

sum = 0
for i in lst[0].split('+'):
    sum += int(i)

for i in lst[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)