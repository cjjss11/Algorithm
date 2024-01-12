def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    # 아직 제거되지 못 한 숫자는 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]  
    for i in stack:
        answer += i

    return answer