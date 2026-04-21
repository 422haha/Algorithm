m = int(input())
n = int(input())
cnt = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i+j == 10:
            cnt += 1

if cnt == 1:
    print("There is 1 way to get the sum 10.")
else:
    print(f"There are {cnt} ways to get the sum 10.")