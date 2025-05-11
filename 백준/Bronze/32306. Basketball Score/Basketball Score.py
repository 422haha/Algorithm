lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

s1 = lst1[0]+lst1[1]*2+lst1[2]*3
s2 = lst2[0]+lst2[1]*2+lst2[2]*3

if s1 > s2:
    print(1)
elif s1 < s2:
    print(2)
else:
    print(0)