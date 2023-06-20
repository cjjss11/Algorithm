import heapq
import sys
input = sys.stdin.readline

N,M,X = map(int,input().split())
lst = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in lst[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

# X에서 출발해서 각각의 마을까지의 경로
to_X = []
for i in range(1,N+1):
    distance = dijkstra(X)
    to_X.append(distance[i])

# 각가의 마을에서 출발해서 X까지의 경로
from_X = []
for i in range(1,N+1):
    distance = dijkstra(i)
    from_X.append(distance[X])

# 두 경로를 더해서 최대값 찾기
max_time = []
for i in range(len(to_X)):
    max_time.append(to_X[i]+from_X[i])
print(max(max_time))