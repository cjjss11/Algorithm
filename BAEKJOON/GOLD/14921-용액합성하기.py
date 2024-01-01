import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
start = 0
end = N-1
minvalue = float('inf')
while start < end:
    sum_value = lst[start] + lst[end]
    if abs(sum_value) < abs(minvalue):
        minvalue = sum_value
    elif sum_value < 0:
        start += 1
    elif sum_value > 0:
        end -= 1
    else:
        break
print(minvalue)
