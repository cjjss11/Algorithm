def solution(begin, target, words):
    global answer,result
    
    if target not in words:
        return 0
    answer = 21e8
    used = [0]*len(words)
    result = 0
    def dfs(change):
        global result,answer
        if change == target:
            if result < answer:
                answer = result
            return
        for i in range(len(words)):
            cnt = 0
            for j in range(len(change)):
                if used[i] == 0:
                    if change[j] != words[i][j]:
                        cnt += 1
            if cnt == 1:
                used[i] = 1
                result += 1
                dfs(words[i])
                used[i] = 0
                result -= 1
    dfs(begin)
    return answer