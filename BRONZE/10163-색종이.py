arr = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(N):
    x,y,width,height = map(int,input().split())
    for j in range(x,x+width):
        for k in range(y,y+height):
            arr[j][k] = i+1
for i in range(N):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if arr[j][k] == i+1:
                cnt += 1
    print(cnt)

# -> pypy로 할 때는 정답이 나오지만 python으로 넣을 때는 시간초과 남