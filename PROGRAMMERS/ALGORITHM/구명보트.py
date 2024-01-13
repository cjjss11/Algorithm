def solution(people, limit):
    answer = 0
    # 가벼운 순으로 정렬
    people.sort()
    start = 0
    end = len(people)-1
    while start <= end:
        # 가벼운 사람이랑 무거운 사람 합이 limit보다 작거나 같으면
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            # 가벼운 사람과 무거운 사람 짝지어서 구출
            answer += 1
        # 가벼운 사람이랑 무거운 사람 합이 limit보다 크면
        else:
            # 무거운 사람부터 구출
            end -= 1
            answer += 1
    return answer