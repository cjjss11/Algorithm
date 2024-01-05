import math
def solution(numbers):
    answer = 0
    number = []
    # numbers를 리스트로 만들기
    for i in range(len(numbers)):
        number.append(numbers[i])
        
    path = [""]*len(numbers)
    used = [0]*len(numbers)
    prime = [] # 모든 조합 담기
    # numbers로 모든 조합 만들기
    # 부분집합이지만 start로 하지 않고 방문배열로 같은 숫자 조합도 다른 숫자로 만들어주기
    # -> ex) 1과 7로 17과 71을 만들 수 있는데 start로 하면 같은 조합이 됨 그래서 방문배열로 다르게 만들기
    def dfs(level):
        if level == len(numbers):
            return
        for i in range(len(numbers)):
            abc = ""
            if used[i] == 0:
                used[i] = 1
                path[level] = numbers[i]
                for j in path:
                    abc += j
                prime.append(abc)
                dfs(level+1)
                path[level] = ""
                used[i] = 0
    dfs(0)  
    
    # 문자열로 되어 있는 값을 숫자로 변형
    for i in range(len(prime)):
        prime[i] = int(prime[i])
    # 중복되는 값 없애기
    prime = list(set(prime))
    
    # 소수 찾기
    def primenumber(num):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                return 0
        return 1
    
    for i in range(len(prime)):
        if prime[i] != 0 and prime[i] != 1:
            result = primenumber(prime[i])
            if result == 1:
                answer += 1
    return answer