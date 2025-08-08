a, b = map(int, input().split())
c, d = map(int, input().split())

print(((((a+b-1)%4)+1+(c+d-1)-1)%4)+1)