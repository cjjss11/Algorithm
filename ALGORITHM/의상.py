def solution(clothes):
    answer = 1
    clothes_dic = {}
    for i in clothes:
        clothes_dic[i[1]] = 1
        
    for i in clothes:
        clothes_dic[i[1]] += 1
    
    lst = []
    # 빈 리스트에 value 길이 값을 넣어줌
    for value in clothes_dic.values():
        lst.append(value)
    
    for i in lst:
        answer *= i
    answer = answer - 1
    
    return answer

# 예를 들어 종류 headgear에 yellow_hat, green_turban 두 개가 있다고 하면
# (0,1,2)로 볼 수 있다
# 0은 두 개 다 안 입은 것을 의미
# 1은 yellow_hat을 썼다는 것을 의미
# 2는 green_turban를 썼다는 것을 의미
# 이런 식으로 모든 종류에 대해 조합을 해보면 각각의 이름+1들을 곱하고 -1한 값이 규칙이 된다.
# 즉, headgear(0,1,2) eyewear(0,1)으로 보면 3 * 2 - 1을 해서 답이 5가 나오는 것이다.