N,M = map(int,input().split())
set1 = set()
set2 = set()
for _ in range(N):
    a = input()
    set1.add(a)
for _ in range(N,(N+M)):
    a = input()
    set2.add(a)
print(len(set1&set2))
people = set1&set2
lst = []
for i in people:
    lst.append(i)
lst.sort()
for i in lst:
    print(i)