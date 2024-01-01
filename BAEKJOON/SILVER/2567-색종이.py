def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1,len(lst)):
            if lst[i-1] != lst[i]:
                cnt += 1
    return cnt
arr = [[0]*102 for _ in range(102)]
N = int(input())
for _ in range(N):
    dx,dy = map(int,input().split())
    for i in range(dy,dy+10):
        for j in range(dx,dx+10):
            arr[i][j] = 1
r_arr = list(zip(*arr)) # 전치행렬
answer = count(arr) + count(r_arr)
print(answer)