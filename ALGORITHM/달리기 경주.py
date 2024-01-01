def solution(players, callings):
    players_dic = {}
    for i in range(len(players)):
        players_dic[players[i]] = i
    for i in callings:
        # 호명된 선수의 등수를 idx로 선언
        idx = players_dic[i]
        # 호명된 선수의 등수를 -1
        players_dic[i] -= 1
        # 호명된 선수 바로 앞에 있던 선수의 등수를 +1
        players_dic[players[idx-1]] += 1
        # players 리스트에서 호명된 선수와 그 앞에 있는 선수의 위치 바꾸기(등수 바꿔주기)
        players[idx-1],players[idx] = players[idx],players[idx-1]
    return players