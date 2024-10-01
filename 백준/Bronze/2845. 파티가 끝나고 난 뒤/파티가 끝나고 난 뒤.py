l, p = map(int, input().split())
c = l*p
for i in map(int, input().split()):
    print(i-c, end=' ')