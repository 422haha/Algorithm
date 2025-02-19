for _ in range(int(input())):
    s, a, b = input().split()
    print(s.replace(s[int(a):int(b)],''))