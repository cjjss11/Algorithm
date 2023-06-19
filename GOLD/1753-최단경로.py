import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
start = int(input())
lst = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    lst[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in lst[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1,N+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])