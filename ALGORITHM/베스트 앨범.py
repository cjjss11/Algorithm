def solution(genres, plays):
    answer = []
    genres_lst = []
    genres_dic = {}

    # 리스트에는 genres 리스트에 있는 각 장르에 대한 재생횟수와 고유번호를 담음
    for i in range(len(genres)):
        genres_lst.append([genres[i], plays[i], i])
        
    # 재생횟수 기준으로 내림차순 정렬, 만약 같다면 고유번호 기준으로 오름차순 정렬
    # x[0]을 넣어야 하는 이유는 같은 장르끼리 모으고, 비교해서 정렬을 진행하기 위해
    # x[0]이 없으면 장르 상관 업시 재생횟수와 고유번호 기준으로 정렬이 됨
    genres_lst = sorted(genres_lst, key=lambda x: (x[0], -x[1], x[2]))

    # 딕셔너리에는 key 값에는 장르와 value 값에는 각 장르의 총 재생횟수를 넣음
    for i in genres_lst:
        if i[0] not in genres_dic:
            genres_dic[i[0]] = i[1]
        else:
            genres_dic[i[0]] += i[1]

    # 정렬 진행 후 딕셔너리가 리스트로 변형됨
    genres_dic = sorted(genres_dic.items(), key=lambda x: x[1], reverse=True)

    for i in genres_dic:
        cnt = 0
        for j in genres_lst:
            # 정렬된 딕셔너리의 장르(i[0])와 정렬된 리스트의 장르[j[0]]이 같으면
            if i[0] == j[0]:
                cnt += 1
                # 한 곡당 두 개까지만 출시한다고 하였으므로
                if cnt <= 2:
                    # 고유번호(j[2])를 정답 리스트에 담기
                    answer.append(j[2])
                else:
                    break
    return answer