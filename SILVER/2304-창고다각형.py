N = int(input())
lst = [0]*1001
maxvalue = 0
max_i = 0
for i in range(N):
    L,H = map(int,input().split())
    lst[L] = H
    if H > maxvalue:
        maxvalue = H
        max_i = L
max_L = 0
ans = 0
max_R = 0
for i in range(max_i+1):
    max_L = max(max_L,lst[i])
    ans += max_L
for i in range(1000,max_i,-1):
    max_R = max(max_R,lst[i])
    ans += max_R
print(ans)