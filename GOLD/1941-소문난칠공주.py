student = [list(input()) for _ in range(5)]
used = [[0]*5 for _ in range(5)]
result = set() # 중복을 제거하기 위해 set으로 풀이
def dfs(Y,S,level,path): # path배열을 전역으로 선언
    if Y > 3:
        return
    if level == 7:
        path.sort() # 튜플은 순서가 없으므로 정렬 필요
        result.add(tuple(path)) # set에 넣으려면 튜플 형태여야 함
        return
    direct_i = [-1,0,1,0]
    direct_j = [0,1,0,-1]
    for y,x in path:
        for i in range(4):
            dy = y + direct_i[i]
            dx = x + direct_j[i]
            if 0 <= dy < 5 and 0 <= dx < 5:
                if used[dy][dx] == 0:
                    if student[dy][dx] == 'S':
                        used[dy][dx] = 1
                        dfs(Y,S+1,level+1,path+[(dy,dx)]) # path 리스트에 튜플 형태 좌표를 리스트로 넣기
                        used[dy][dx] = 0
                    elif student[dy][dx] == 'Y':
                        used[dy][dx] = 1
                        dfs(Y+1,S,level+1,path+[(dy,dx)])
                        used[dy][dx] = 0

for i in range(5):
    for j in range(5):
        if used[i][j] == 0:
            if student[i][j] == 'S':
                used[i][j] = 1
                dfs(0,1,1,[(i,j)]) # 좌표를 넣고 시작했으므로 level 1부터 시작
            elif student[i][j] == 'Y':
                used[i][j] = 1
                dfs(1,0,1,[(i,j)])
print(len(result))