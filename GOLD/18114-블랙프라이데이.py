N,C = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
def binary_search(start,end,C):
    while 1:
        mid = (start + end) // 2
        if lst[mid] == C:
            return 1
        if lst[mid] < C:
            start = mid + 1
        elif lst[mid] > C:
            end = mid - 1
        if start > end:
            return 0

flag = 0
start = 0
end = N-1
if binary_search(start,end,C):
    flag = 1
if flag:
    print(1)
else:
    while start < end:
        sum_value = lst[start] + lst[end]
        if sum_value == C:
            flag = 1
            break
        elif sum_value > C:
            end -= 1
        elif sum_value < C:
            # 최대 3개까지이므로 남은 한 개 값 확인
            value = C - sum_value
            # 쓰여진 값은 다시 못 씀
            if lst[start] != value and lst[end] != value:
                if binary_search(start,end,value):
                    flag = 1
                    break
            start += 1
    if flag == 1:
        print(1)
    else:
        print(0)