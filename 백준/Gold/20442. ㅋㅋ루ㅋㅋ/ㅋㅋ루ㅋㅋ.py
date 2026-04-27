import sys

lst = list(map(str, sys.stdin.readline().rstrip()))
lst_l = []      # 왼쪽에서부터의 'K'의 개수를 저장할 리스트
lst_r = []      # 오른쪽에서부터의 'K'의 개수를 저장할 리스트

temp = 0
for i in lst:   # 오른쪽부터 순회하며 'K'의 개수를 세서 lst_r에 저장
    if i == 'K':
        temp += 1
    else:
        lst_l.append(temp)
temp = 0
for i in lst[::-1]:
    if i == 'K':
        temp += 1
    else:
        lst_r.append(temp)
lst_r.reverse() # 역순으로 저장되어 있으므로 다시 뒤집어 줌

i, j = 0, len(lst_r)-1
res = 0

while i <= j:
    temp = j-i+1+2*min(lst_l[i], lst_r[j])  # 구간 길이 계산
    if res < temp:
        res = temp
    if lst_l[i] < lst_r[j]:
        i += 1
    else:
        j -= 1

print(res)