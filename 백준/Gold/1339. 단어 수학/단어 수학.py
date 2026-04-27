import sys

n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dct = {}    # 단어별 알파벳 출현 횟수
temp = []   # 숫자 저장

for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] in dct:
            dct[arr[i][j]] += 10 ** (len(arr[i])-j-1)
        else:
            dct[arr[i][j]] = 10 ** (len(arr[i])-j-1)

for i in dct.values():
    temp.append(i)
temp.sort(reverse=True)

res = 0
num = 9
for i in temp:
    res += num * i
    num -= 1
print(res)