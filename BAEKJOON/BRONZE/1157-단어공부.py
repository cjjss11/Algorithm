lst = input().upper()
word = {}
for i in lst:
    if i not in word:
        word[i] = 1
    else:
        word[i] += 1
maxvalue = -21e8
ans = []
for key,value in word.items():
    if value >= maxvalue:
        maxvalue = value
for key,value in word.items():
    if value == maxvalue:
        ans.append(key)
if len(ans) > 1:
    print('?')
else:
    print(ans[0])