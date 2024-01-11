def solution(word):
    answer = 0
    lst = ['A','E','I','O','U']
    path = ['']*5
    used = [0]*5
    result = []
    def dfs(level):
        if level == 5:
            return
        for i in range(5):
            path[level] = lst[i]
            abc = ''
            for i in path:
                abc += i
            result.append(abc)
            dfs(level+1)
            path[level] = ""
    dfs(0)
    for i in range(len(result)):
        if result[i] == word:
            answer = i+1
    return answer