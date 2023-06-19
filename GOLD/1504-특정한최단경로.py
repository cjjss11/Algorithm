import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))
    lst[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in lst[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
    return distance

# 1에서 각 정점까지의 최단 경로 계산
dist_from_1 = dijkstra(1)

# v1에서 각 정점까지의 최단 경로 계산
dist_from_v1 = dijkstra(v1)

# v2에서 각 정점까지의 최단 경로 계산
dist_from_v2 = dijkstra(v2)


# 1 -> v1 -> v2 -> N 경로와 1 -> v2 -> v1 -> N 경로 중 더 짧은 경로 선택
route1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
route2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]
result = min(route1,route2)

if result >= INF:
    result = -1
print(result)
