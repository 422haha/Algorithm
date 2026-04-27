text = []

for i in range(5):
    text.append(input())

for j in range(15):
    for k in range(5):
        if j < len(text[k]):
            print(text[k][j], end='')
        else:
            print('', end='')