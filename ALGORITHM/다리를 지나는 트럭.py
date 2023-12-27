from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge = deque([0] * bridge_length) # 다리 길이만큼 만들기
    currentWeight = 0
    while bridge:
        answer += 1
        currentWeight -= bridge.popleft()
        if q:
            if currentWeight + q[0] <= weight: # 현재 무게에서 그다음 나올 무게를 합한 것이 작거나 같으면 현재 무게에 더함
                currentWeight += q[0]
                bridge.append(q.popleft())     # 다리 리스트에 추가
            else:
                bridge.append(0)               # 현재 무게에서 그다음 나올 무게를 합한 것이 크면 다리 리스트에 0을 추가
    return answer