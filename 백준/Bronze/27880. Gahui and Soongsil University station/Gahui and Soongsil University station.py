res = 0
for _ in range(4):
    step, cnt = input().split()
    res += int(cnt)*[21, 17][step =='Stair']
print(res)