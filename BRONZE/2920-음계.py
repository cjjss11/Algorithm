lst = list(map(int,input().split()))
result = ''
cnt = 1
r_cnt = 1
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        cnt += 1
for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        r_cnt += 1
if cnt == len(lst):
    result = 'ascending'
elif r_cnt == len(lst):
    result = 'descending'
else:
    result = 'mixed'
print(result)
