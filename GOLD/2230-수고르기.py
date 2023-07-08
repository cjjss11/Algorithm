N,M = map(int,input().split())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

lst.sort()
end = 0
start = 0
minvalue = 21e8
while start < N and end < N:
    value = lst[end] - lst[start]
    if value >= M:
        if value < minvalue:
            minvalue = value
        start += 1
    elif value < M:
        end += 1
print(minvalue)