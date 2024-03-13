import sys
init = ['***', '* *', '***'] # 초기 별찍기 패턴


def generate_pattern(size=3, pattern_array=init):
    if size == n:   # 원하는 높이에 도달 -> 패턴을 반환
        return pattern_array
    tmp = []
    for pattern in pattern_array:
        tmp.append(pattern * 3)
    for pattern in pattern_array:
        tmp.append(pattern + ' ' * size + pattern)
    for pattern in pattern_array:
        tmp.append(pattern * 3)
    return generate_pattern(size * 3, tmp)


n = int(sys.stdin.readline().rstrip())
res = generate_pattern(3, init)

for i in res:
    print(i)