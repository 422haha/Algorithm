i = 0
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    i += 1
    print('Case %d: Sorting... done!' %(i))