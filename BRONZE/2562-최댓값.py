lst = []
for i in range(9):
    num = int(input())
    lst.append(num)
maxvalue = -21e8
max_i = 0
for i in range(len(lst)):
    if lst[i] > maxvalue:
        maxvalue = lst[i]
        max_i = i+1
print(maxvalue)
print(max_i)