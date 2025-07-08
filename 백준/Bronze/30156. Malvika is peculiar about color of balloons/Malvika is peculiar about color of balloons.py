for _ in range(int(input())):
    s = input().strip()
    print(min(s.count('a'), s.count('b')))