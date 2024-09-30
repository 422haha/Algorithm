d, h, m = map(int, input().split())
t = m-11+(h-11)*60+(d-11)*1440

print(t if t >= 0 else -1)