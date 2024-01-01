T = 10
for test_case in range(1, T + 1):
    dump_range = int(input())
    dump_lst = list(map(int, input().split()))
    maxvalue = dump_lst[0]
    minvalue = dump_lst[0]
    n = 1
    min_idx = 0
    max_idx = 0
    while n < dump_range + 1:
        for j in range(len(dump_lst)):
            if maxvalue < dump_lst[j]:
                maxvalue = dump_lst[j]
                max_idx = j
            if minvalue > dump_lst[j]:
                minvalue = dump_lst[j]
                min_idx = j
        maxvalue = maxvalue - 1
        dump_lst[max_idx] = maxvalue
        minvalue = minvalue + 1
        dump_lst[min_idx] = minvalue
        n += 1
    maxvalue1 = dump_lst[0]
    minvalue1 = dump_lst[0]
     
    for i in range(len(dump_lst)):
        if maxvalue1 < dump_lst[i]:
            maxvalue1 = dump_lst[i]
        if minvalue1 > dump_lst[i]:
            minvalue1 = dump_lst[i]
    print(f'#{test_case} {maxvalue1-minvalue1}')