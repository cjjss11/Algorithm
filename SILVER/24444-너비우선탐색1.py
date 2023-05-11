import sys
from collections import deque
input = sys.stdin.readline
N,M,R = map(int,input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for lst in arr:
    lst.sort()

used = [0]*(N+1) # 방문 배열
used[R] = 1

result = [0]*(N+1) # 방문 순서 담을 배열
result[R] = 1 # 시작 정점 체크 하기
idx = 1

q = deque()
q.append(R)

while q:
    now = q.popleft()
    for i in arr[now]:
        if used[i] == 0:
            idx += 1
            result[i] = idx # 배열에 있는 값을 인덱스로
            used[i] = 1
            q.append(i)
            
for i in result[1:]:
    print(i)

