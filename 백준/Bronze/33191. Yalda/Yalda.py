b = int(input())

w = int(input())
p = int(input())
n = int(input())

if b >= w:
    print("Watermelon")
elif b >= p:
    print("Pomegranates")
elif b >= n:
    print("Nuts")
else:
    print("Nothing")