uapc = "UAPC"
s = input()

res = ""
temp = 0

for i in uapc:
    if temp < len(s) and i == s[temp]:
        temp += 1
    else:
        res += i

print(res)