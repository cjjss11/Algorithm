from heapq import heappush, heappop
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        a,num = i.split()
        num = int(num)
        if a == 'I':
            heappush(heap,num)
        elif a == 'D' and num == 1:
            if len(heap) != 0:
                maxvalue = max(heap)
                heap.remove(maxvalue)
        elif a == 'D' and num == -1:
            if len(heap) != 0:
                heappop(heap)
    if len(heap) == 0:
        answer = [0,0]
    else:
        answer = [max(heap),heappop(heap)]
        
    return answer