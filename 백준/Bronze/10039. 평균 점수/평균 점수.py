res = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        res += 40
    else:
        res += score

print(res//5)