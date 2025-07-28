for i in range(1, int(input())+1):
    n, x = map(int, input().split())
    remainder = n%x
    print(f"Case {i}: {remainder}")