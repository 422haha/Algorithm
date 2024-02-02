import sys

s = sys.stdin.readline().rstrip()
s_set = set()

# 부분 문자열 슬라이싱으로 구하기
for i in range(0, len(s)):
    for j in range(i, len(s)):
        s_set.add(s[i:j+1])

print(len(s_set))