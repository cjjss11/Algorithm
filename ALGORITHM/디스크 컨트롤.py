from heapq import heappush, heappop
# from heapq만 적으면 heapq.heappush, heapq.heappop으로 해야 함
def solution(jobs):
    answer = 0 # 총 작업 소요 시간
    now = 0 # 현재 시점
    i = 0
    start = -1 # 바로 이전에 작업을 완료한 시간
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            # 현재 시점에서 처리할 수 있는 작업을 heap에 담기
            if start < j[0] <= now:
                # 소요 시간 기준으로 최소힙을 사용하기 때문에
                # [작업 소요 시간, 작업 요청 시간] 순서로 heap에 담기
                heappush(heap, [j[1],j[0]])
        if heap: # 처리할 작업이 남아 있으면
            time = heappop(heap)
            start = now
            now += time[0]
            answer += now - time[1]
            i += 1
        else:
            # 처리할 작업이 없는 경우 다음 시간으로 넘어갈 수 있게 now에 + 1 해줌
            now += 1
    answer = answer // len(jobs)
    return answer