def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    # 가장 큰 수를 구해야 하므로 맨 앞 자리에 올 때 가장 큰 수를 만들 수 있는 값을 찾기
    # numbers의 원소는 1000이하이므로 모든 원소에 *3을 해서 최소 3자리 이상 만들기
    for i in range(len(numbers)):
        a = numbers[i]*3
        numbers[i] = a
    # 문자열 형태인 숫자를 정렬하면 크기로 인식하는 것이 아닌 순서로 인식하기 때문에
    # 내림차순 정렬을 하면 앞자리가 가장 큰 수가 앞으로 옴 
    numbers = sorted(numbers, key=lambda x:x, reverse=True)
    for i in range(len(numbers)):
        # 3을 곱해서 3자리 이상 만들었기 때문에 원래 값을 구하기 위해 나누기 3을 함
        a = len(numbers[i]) // 3
        # 정렬된 numbers에서 원래 값들을 answer에 더해서 가자 큰 수를 구함
        answer += numbers[i][:a]
    # [0,0,0]을 입력하면 값이 000이 나오기 때문에 조건을 넣어서 처리해줌
    if int(answer) == 0:
        answer = '0'
    return answer