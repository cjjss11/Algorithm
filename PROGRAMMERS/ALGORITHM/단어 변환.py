# 첫 번째 방법 dfs 풀이
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

# 두 번째 방법 bfs 풀이
from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    used = [0] * len(words)
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            word_cnt = 0
            if used[i] == 0:
                for j in range(len(word)):
                    if words[i][j] != word[j]:
                        word_cnt += 1
                if word_cnt == 1:
                    q.append((words[i], cnt+1))
                    used[i] = 1
    return answer