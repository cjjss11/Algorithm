T = int(input())
for test_case in range(1,T+1):
    lst = list(input())
    idx = 0
    while 1:
        if idx >= len(lst)-1:
            break
        if lst[idx] == lst[idx+1]:
            lst.pop(idx)
            lst.pop(idx)
            idx = 0
        else:
            idx += 1
    print(f'#{test_case} {len(lst)}')