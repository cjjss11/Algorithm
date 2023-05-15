import sys
N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
X = int(sys.stdin.readline())
cnt = 0
end = N-1
start = 0
lst_sum = 0
while start < end: # start가 end보다 작은 동안에만 반복
    lst_sum = lst[start] + lst[end]
    if lst_sum == X:
        cnt += 1
        start += 1
        end -= 1
    elif lst_sum < X: # 합이 X보다 작으면 start를 오른쪽으로 이동
        start += 1
    elif lst_sum > X: # 합이 X보다 크면 end를 왼쪽으로 이동
        end -= 1
print(cnt)
