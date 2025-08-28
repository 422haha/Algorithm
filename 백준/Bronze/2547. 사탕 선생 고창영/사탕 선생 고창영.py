for _ in range(int(input())):
    input()
    n = int(input())
    res = 0
    for _ in range(n):
        res += int(input())
    if res%n == 0:
        print("YES")
    else:
        print("NO")