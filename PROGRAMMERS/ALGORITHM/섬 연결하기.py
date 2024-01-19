# 유니온 파인드
def findParent(parent, x):
    if parent[x] == x:
        return x
    else:
        return findParent(parent, parent[x])

def setUnion(parent,a, b):
    fa = findParent(parent, a)
    fb = findParent(parent, b)
    
    if fa == fb:
        return
    else:
        parent[fb] = fa

def solution(n, costs):
    answer = 0
    parent = [0]*n
    for i in range(n):
        parent[i] = i
    costs.sort(key=lambda x:x[2])
    # 크루스칼
    for a,b,cost in costs:
        if findParent(parent, a) != findParent(parent, b):
            setUnion(parent, a, b)
            answer += cost
    return answer