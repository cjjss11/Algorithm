arr = [[0]*100 for _ in range(100)]
for i in range(4):
    dx1,dy1,dx2,dy2 = map(int,input().split())
    for i in range(dy1,dy2):
        for j in range(dx1,dx2):
            arr[i][j] = 1
count = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1
print(count)