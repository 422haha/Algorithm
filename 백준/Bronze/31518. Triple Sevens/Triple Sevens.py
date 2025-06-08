n = int(input())

lst = []
for _ in range(3):
    temp = set(map(int, input().split()))
    lst.append(temp)

if all(7 in i for i in lst):
    print(777)
else:
    print(0)
