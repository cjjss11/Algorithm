N,K = map(int,input().split())
bag = [[0 for _ in range(K+1)] for _ in range(N+1)]

item = [[0,0]]
for _ in range(N): # 아이템 입력
    W,V = map(int,input().split())
    item.append([W,V])

for i in range(1,N+1): # 아이템 개수 만큼 반복
    for j in range(1,K+1): # 최대 무게까지 반복
        weight = item[i][0]
        value = item[i][1]
        if weight > j: # 가방에 넣을 수 없으면
            bag[i][j] = bag[i-1][j] # 위에 값 그대로 가져오기
        else:          # 가방에 넣을 수 있으면
            # 위에 값과 현재 아이템 가치 + 그 전 단계에서 구한 남은 무게의 가치 중 큰 값 넣기
            bag[i][j] = max(bag[i-1][j], value + bag[i-1][j-weight])

maxvalue = -21e8
for i in range(N+1):
    for j in range(K+1):
        if bag[i][j] > maxvalue:
            maxvalue = bag[i][j]
print(maxvalue)