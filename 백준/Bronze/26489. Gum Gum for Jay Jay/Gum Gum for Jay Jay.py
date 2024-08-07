res = 0

while True:
    try:
        gum_gum = input()
        res += 1
    except EOFError:
        break

print(res)