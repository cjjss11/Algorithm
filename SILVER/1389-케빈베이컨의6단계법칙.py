from collections import deque
N,M = map(int,input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)
for lst in arr:
    lst.sort()
def bfs(st):
    q = deque()
    q.append(st)
    used = [0]*(N+1) # 1부터 다 합을 구해야 하기 때문에 들어올 때 마다 방문 배열 초기화
    used[st] = 1
    sum = 0
    while q:
        now = q.popleft()
        for i in arr[now]:
            if used[i] == 0:
                used[i] = used[now] + 1 # 몇 단계를 거치는지 알기 위해
                q.append(i)
    for i in used: # 방문 배열 값을 다 더함
        sum += i
    return sum
result = [] 
for i in range(1,N+1):
    ans = bfs(i)
    result.append(ans)
minvalue = 21e8
min_idx = 21e8
for i in range(len(result)):
    if result[i] == minvalue: # 최솟값이 여러 개이면 최소 인덱스 구하기
        if i < min_idx:
            min_idx = i
    elif result[i] < minvalue:
        minvalue = result[i]
        min_idx = i
print(min_idx+1)