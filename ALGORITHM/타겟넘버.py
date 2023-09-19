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