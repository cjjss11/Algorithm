def solution(k, dungeons):
    global maxx
    answer = -1
    maxx = -21e8
    used = [0]*len(dungeons)
    def dfs(level, cnt, hp):
        global maxx
        if level == len(dungeons):
            if cnt > maxx:
                maxx = cnt
            return
        for i in range(len(dungeons)):
            a = dungeons[i][0]
            b = dungeons[i][1]
            # 최소 필요도 a가 현재 피로도 hp 보다 작거나 같고 방문한 적이 없으면
            if a <= hp and used[i] == 0:
                used[i] = 1
                # 다음 단계, 개수 카운트, 현재 피로도에서 소모 피로도 뺀 값
                dfs(level+1, cnt+1, hp-b)
                used[i] = 0
            # 최소 필요도 a가 현재 피로도 hp 보다 큰 경우이지만 방문한 적이 없으면
            else:
                if used[i] == 0:
                    used[i]= 1
                    # 다음 단계로만
                    dfs(level+1, cnt, hp)
                    used[i] = 0

    dfs(0,0, k)
    answer = maxx
    return answer