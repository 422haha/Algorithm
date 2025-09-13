n = int(input())
lst = list(map(int, input().split()))
line = [0]*n

for i in range(n):
    temp = 0
    for j in range(n):
        if temp == lst[i] and line[j] == 0:
            line[j] = i+1
            break
        elif line[j] == 0:
            temp += 1

print(*line)