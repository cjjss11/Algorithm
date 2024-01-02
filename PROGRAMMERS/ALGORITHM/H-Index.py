# 첫 번째 방법
def solution(citations):
    answer = 0
    num = 1
    citations = sorted(citations, key=lambda x:x, reverse=True)
    for i in citations:
        if i >= num:
            answer = num
            num += 1
    return answer

# 두 번째 방법
def solution(citations):
    citations = sorted(citations, key=lambda x:x, reverse=True)
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)