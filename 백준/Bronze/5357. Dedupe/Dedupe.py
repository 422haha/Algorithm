n = int(input())

for _ in range(n):
    s = list(input())
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            print(s[i], end="")
    print(s[len(s)-1])