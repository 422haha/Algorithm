import sys


def train(epm, cnt):
    global temp, target
    time = 0
    for _ in range(cnt):
        gain = epm*30
        if temp+gain >= target:
            need = target-temp
            need_time = (need+epm-1)//epm
            temp = target
            return time+need_time
        temp += gain
        time += 30
    return time


a, b, c = map(int, sys.stdin.readline().split())
s, v = map(int, sys.stdin.readline().split())
l = int(sys.stdin.readline())

target = (250-l)*100
temp = 0
res = 0

res += train(c, v)          # VIP
if temp >= target:
    print(res)
    sys.exit(0)

res += train(b, s)          # 심신
if temp >= target:
    print(res)
    sys.exit(0)

res += (target-temp+a-1)//a # 이벤트 맵

print(res)
