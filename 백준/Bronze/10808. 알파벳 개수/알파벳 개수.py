s = input()

res = [0]*26
for c in s:
    res[ord(c)-97] += 1

print(*res)