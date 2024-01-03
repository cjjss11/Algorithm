def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        # 가로 길이가 세로 길이보다 짧으면 가로 길이와 세로 길이를 서로 바꿔줌
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
    w_max = -21e8
    h_max = -21e8
    
    for i in range(len(sizes)):
        # 가로 길이 중 최댓값 찾기
        if sizes[i][0] > w_max:
            w_max = sizes[i][0]
        # 세로 길이 중 최댓값 찾기
        if sizes[i][1] > h_max:
            h_max = sizes[i][1]
    answer = w_max * h_max
    return answer