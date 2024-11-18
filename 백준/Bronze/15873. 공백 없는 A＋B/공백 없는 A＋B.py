n = input()

if len(n) == 2:
    print(sum(map(int, list(n))))
elif len(n) == 4:
    print(20)
elif n[1] == "0":
    print(sum([int(n[:2]), int(n[2])]))
else:
    print(sum([int(n[0]), int(n[1:3])]))