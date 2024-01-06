def solution(brown, yellow):
    answer = []
    lst = []
    w = 0
    h = 0
    # brown과 yellow 더한 값으로 약수 찾기
    def divisor(num):
        for i in range(1,num+1):
            if (num % i == 0):
                lst.append(i)
    divisor(brown+yellow)
    # 리스트 길이가 홀수라는 것은 똑같은 숫자가 두 번 들어가야 한다는 의미이므로
    # ex) 9의 약수 3
    
    if len(lst) % 2 == 1:
        num = lst[len(lst)//2]
        lst.append(num)
    lst.sort()
    
    # 리스트 절반 길이만큼 범위를 동안
    for i in range(len(lst)//2):
        a = lst[i]
        b = lst[-(i+1)]
        # 짝이 되는 값끼리 테두리 개수를 구하고 그 개수가 brown이랑 같으면
        if ((b*2)+(a-2)*2) == brown:
            w = b
            h = a
            # break를 안 하면 답을 찾아도 그다음으로 넘어가서 그 값으로 갱신이 되어버려 답이 틀림
            break
    answer = [b,a]
    return answer