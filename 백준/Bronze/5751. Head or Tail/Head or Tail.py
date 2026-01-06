while True:
    n = int(input())
    if not n:
        break
    lst = list(map(int, input().split()))
    print(f'Mary won {lst.count(0)} times and John won {lst.count(1)} times')