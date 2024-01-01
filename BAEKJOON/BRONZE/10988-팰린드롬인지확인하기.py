lst = input()
r_lst = []
flag = 0
for i in range(len(lst)-1,-1,-1):
    r_lst.append(lst[i])
for i in range(len(lst)):
    if lst[i] != r_lst[i]:
        flag = 1
if flag:
    print(0)
else:
    print(1)