N = int(input())
lst = list(map(int,input().split()))
lst.sort()
end = N-1
start = 0
min_lst = [lst[start],lst[end]]
minvalue = 21e8
while start < end:
    sum_value = lst[start] + lst[end]
    if abs(sum_value) < minvalue:
        minvalue = abs(sum_value)
        min_lst = [lst[start],lst[end]]
    if sum_value < 0:
        start += 1
    else:
        end -= 1
print(min_lst[0],min_lst[1])
