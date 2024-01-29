n = int(input())
cnt = 0
title = 665

while title > 0:
    if '666' in str(title):
        cnt += 1
        if cnt == n:
            break
    title += 1

print(title)