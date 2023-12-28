from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    # scoville을 heap 정렬하였으므로 첫 번째 요소가 가장 작은 값이 됨
    # 최솟값이 K보다 작을 동안
    while scoville[0] < K:
        # scoville 길이는 2이상이어야 하므로
        if len(scoville) > 1:
            first = heappop(scoville)
            second = heappop(scoville)
            new_food = first + (second * 2)
            heappush(scoville,new_food)
            answer += 1
        else:
            # answer = -1을 하면 시간초과가 나므로 return -1하고 바로 출력
            return -1
    
    return answer