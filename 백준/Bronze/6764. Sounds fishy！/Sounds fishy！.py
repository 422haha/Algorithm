lst = [int(input()) for _ in range(4)]
temp = 0
for i in range(3):
    if lst[i] < lst[i+1]:
        temp += 1
    elif lst[i] > lst[i+1]:
        temp -= 1

if len(set(lst)) == 1:
    print("Fish At Constant Depth")
elif temp == 3:
    print("Fish Rising")
elif temp == -3:
    print("Fish Diving")
else:
    print("No Fish")