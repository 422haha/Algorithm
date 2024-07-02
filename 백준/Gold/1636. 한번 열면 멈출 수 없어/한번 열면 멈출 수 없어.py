import sys

n = int(sys.stdin.readline().rstrip())
lst = []
current_min, current_max = map(int, sys.stdin.readline().rstrip().split())
total_stress, cnt = 0, 0

for i in range(n-1):
    next_min, next_max = map(int, sys.stdin.readline().rstrip().split())
    if current_max < next_min:
        total_stress += next_min - current_max
        for _ in range(cnt+1):
            lst.append(current_max)
        cnt = 0
        current_min, current_max = next_min, next_min
    elif current_min > next_max:
        total_stress += current_min - next_max
        for _ in range(cnt+1):
            lst.append(current_min)
        cnt = 0
        current_min, current_max = next_max, next_max
    else:   # 현재 프링글스와 다음 프링글스가 겹치는 경우
        current_min = max(current_min, next_min)
        current_max = min(current_max, next_max)
        cnt += 1

print(total_stress)
for _ in range(cnt + 1):
    lst.append(current_min)

for i in lst:
    print(i)