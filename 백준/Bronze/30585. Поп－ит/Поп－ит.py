h, w = map(int, input().split())

cnt_0 = 0
cnt_1 = 0

for _ in range(h):
    s = input().strip()
    cnt_0 += s.count('0')
    cnt_1 += s.count('1')

print(min(cnt_0, cnt_1))
