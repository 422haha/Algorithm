import sys

res = list(str(sys.stdin.readline().rstrip()))
temp = list(str(sys.stdin.readline().rstrip()))
flag = 0

while temp:
    if temp[-1] == 'A':     # 제일 끝의 알파벳이 A라면
        temp.pop()          # A제거
    elif temp[-1] == 'B':   # B라면
        temp.pop()
        temp.reverse()      # 제거 후 뒤집기
    if res == temp:         # 값이 같아지면 break
        flag = 1
        break

print(flag)