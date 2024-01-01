N = int(input())
lst = list(map(int,input().split()))
answer = 0
lst.sort(reverse=True)
for i in range(1, N+1):
    answer += i * lst[i-1]
print(answer)