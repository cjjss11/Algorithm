N,M = map(int,input().split())
height = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    short, tall = map(int,input().split())
    height[tall][short] = 1

# 플로이드 와샬
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if height[i][k] == 1 and height[k][j] == 1:
                height[i][j] = 1     # 자신보다 작은 경우

answer = 0
for i in range(1,N+1):
    check = 0
    for j in range(1,N+1):
        # 자신보다 작은 사람과 큰 사람의 합
        check += (height[i][j] + height[j][i])
    if check == (N-1):    # 자신의 키 순서를 아는 경우
        answer += 1
print(answer)