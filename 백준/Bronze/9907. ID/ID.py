n = input()
weights = [2, 7, 6, 5, 4, 3, 2]
mapping = "JABCDEFGHIZ"

res = 0
for i in range(7):
    res += int(n[i])*weights[i]

print(mapping[res%11])