import sys
input = sys.stdin.readline
import heapq
N = int(input())
heap = []
for _ in range(N):
    for i in map(int,input().split()):
        if len(heap) >= N:
            heapq.heappushpop(heap,i)
        else:
            heapq.heappush(heap,i)
print(heapq.heappop(heap))