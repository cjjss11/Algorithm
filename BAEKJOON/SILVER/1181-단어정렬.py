N = int(input())
S = set()
for _ in range(N):
    word = input()
    S.add(word)
result = sorted(S, key=lambda x:(len(x),x))
for i in result:
    print(i)