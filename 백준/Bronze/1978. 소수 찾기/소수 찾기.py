n = int(input())
lst = list(map(int, input().split()))
num = 0

for i in lst:
    bool = True
    if i == 1:
        bool = False
    else:
        for j in range(2, i):
            if i % j == 0:
                bool = False
    if bool == True:
            num += 1

print(num)