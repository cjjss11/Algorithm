N,X = map(int,input().split())
visit = list(map(int,input().split()))
visit_sum = 0
max_cnt = 1 # 최대 방문을 가진 날이 몇 개 있는지
for i in range(X):
    visit_sum += visit[i]
maxvalue = visit_sum
for i in range(N-X):
    visit_sum += visit[i+X]
    visit_sum -= visit[i]
    if visit_sum > maxvalue:
        maxvalue = visit_sum
        max_cnt = 1
    elif visit_sum == maxvalue:
        max_cnt += 1
if maxvalue == 0:
    print('SAD')
else:
    print(maxvalue)
    print(max_cnt)