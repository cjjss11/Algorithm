N = int(input())
lst = list(map(int,input().split()))
lst.sort()
end = N-1
start = 0
min_lst = [lst[start],lst[end]]
minvalue = 21e8
while start < end:
    sum_value = lst[start] + lst[end]
    if abs(sum_value) < minvalue: # 두 개의 합의 절댓값 최소 비교
        minvalue = abs(sum_value)
        min_lst = [lst[start],lst[end]]
    if sum_value < 0: # 두 개의 합이 음수이면
        start += 1 # start를 이동
    else:             # 두 개의 합이 양수이면
        end -= 1   # end를 이동
print(min_lst[0],min_lst[1])
