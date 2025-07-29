while True:
    n = int(input())
    if n == 0:
        break
    lst = [int(input()) for _ in range(n)]
    while lst:
        print(lst.pop())
    print(0)