while 1:
    flag = 0
    lst = list(map(int,input()))
    r_lst = lst[:]
    if len(lst) == 1 and lst[0] == 0:
        break
    r_lst.reverse()
    for i in range(len(lst)):
        if lst[i] != r_lst[i]:
            flag = 1
            break
    if flag:
        print('no')
    else:
        print('yes')