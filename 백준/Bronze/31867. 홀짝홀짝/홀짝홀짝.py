_ = input()
number = input()

even_count = 0
odd_count = 0

for digit in number:
    if int(digit)%2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print(0)
elif odd_count > even_count:
    print(1)
else:
    print(-1)