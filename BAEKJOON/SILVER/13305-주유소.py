N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

minvalue = 21e8
result = 0

for i in range(N-1):
    if price[i] < minvalue:
        minvalue = price[i]
    result += minvalue * distance[i]

print(result)