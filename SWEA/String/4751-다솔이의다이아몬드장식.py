T = int(input())
for test_case in range(1, T + 1):
    arr = [[] for _ in range(5)]
    lst = list(input())
    a = '..#.'
    b = '.#.#'
    c = '.#.'
    for i in range(len(lst)):
        arr[2] += c
        arr[2] += lst[i]
    arr[2] += c
    arr[2].pop(0)
    arr[2].pop(-1)
    for _ in range(len(lst)):
        arr[0] += a
        arr[1] += b
        arr[3] += b
        arr[4] += a
    arr[0] += '.'
    arr[1] += '.'
    arr[3] += '.'
    arr[4] += '.'
 
    for i in arr:
        for j in i:
            print(j,end='')
        print()