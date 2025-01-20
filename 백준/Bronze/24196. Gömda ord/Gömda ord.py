s = input()
idx = 0

while idx < len(s):
    print(s[idx], end="")
    idx += ord(s[idx]) - 64
