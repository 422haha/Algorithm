n = int(input())
words = input().split()

res = ""
temp = 0

for i, word in enumerate(words):
    if i == 0:
        res += word[0]
    else:
        if temp > len(word):
            res += " "
        else:
            res += word[temp-1]
    temp = len(word)

print(res)