c_score, s_score = 100, 100

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        s_score -= a
    elif a < b:
        c_score -= b

print(c_score)
print(s_score)