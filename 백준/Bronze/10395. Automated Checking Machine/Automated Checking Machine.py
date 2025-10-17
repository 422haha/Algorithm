x = list(map(int, input().split()))
y = list(map(int, input().split()))

flag = True
for i in range(5):
    if x[i]+y[i] != 1:
        flag = False
        break

if flag:
    print("Y")
else:
    print("N")