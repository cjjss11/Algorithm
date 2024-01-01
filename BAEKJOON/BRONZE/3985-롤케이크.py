L = int(input())
N = int(input())
cake = [0]*(L+1)
for i in range(1,len(cake)):
    cake[i] = 1
max1 = -21e8 # 가장 많은 조각을 받을 것으로 예상
max_i1 = 0 #
max2 = -21e8 # 실제로 가장 많은 조각을 받은
max2_i2 = 0
for i in range(N):
    s,e = map(int,input().split())
    if (e-s) == max1:
        if max_i1 > i+1:
            max_i1 = i+1
    elif (e-s) > max1:
        max1 = (e-s)
        max_i1 = i+1
    cnt = 0
    for j in range(s,e+1):
        if cake[j] == 1:
            cnt += 1
            cake[j] = 0
    if cnt > max2:
        max2 = cnt
        max2_i2 = i+1
print(max_i1)
print(max2_i2)