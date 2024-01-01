def solution(phone_book):
    answer = True
    phone_book.sort()  # 문자형 숫자를 정렬하면 숫자를 순서로 인식
    for i in range(len(phone_book)-1):
        N = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:N]: # 그다음 전화번호에서 현재 전화번호 길이만큼 비교
            answer = False
            break
    return answer