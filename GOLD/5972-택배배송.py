import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    # 양방향
    lst[a].append((b,c))
    lst[b].append((a,c))

def dijkstra(start):
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
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
print(distance[N])