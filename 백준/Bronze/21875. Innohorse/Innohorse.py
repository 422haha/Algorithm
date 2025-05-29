ac, ar = input()
bc, br = input()
print(*sorted((abs(ord(ac)-ord(bc)), abs(int(ar)-int(br)))))