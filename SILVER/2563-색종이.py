N = int(input())
arr = [[0]*100 for _ in range(100)]
for i in range(N):
    dx,dy = map(int,input().split())
    for i in range(dy,dy+10):
        for j in range(dx,dx+10):
            arr[i][j] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)
