def solution(nums):
    N = len(nums)
    set_nums = list(set(nums)) # 중복 제거
    answer = 0
    if N//2 < len(set_nums):   # 가져갈 수 있는 마리 수가 포켓몬 종 수 보다 작으면
        answer = N//2  
    elif N//2 > len(set_nums): # 가져갈 수 있는 마리 수가 포켓몬 종 수 보다 크면
        answer = len(set_nums)
    else:                      # 가져갈 수 있는 마리 수와 포켓몬 종 수가 같으면
        answer = N//2
    return answer
