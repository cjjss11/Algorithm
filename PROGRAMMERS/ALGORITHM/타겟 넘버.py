# 1. 첫 번째 방법
def solution(numbers, target):
    global answer
    
    answer = 0
    def dfs(level,sum):
        global answer
        if level == len(numbers):
            if sum == target:
                answer += 1
            return
        dfs(level+1, sum+numbers[level])
        dfs(level+1, sum-numbers[level])
    dfs(0,0)
    return answer

# 2. 두 번째 방법
def solution(numbers, target):
    result = [0]
    for number in numbers:
        data = []
        for value in result:
            data.append(value + number)
            data.append(value - number)
        result = data
    return result.count(target)