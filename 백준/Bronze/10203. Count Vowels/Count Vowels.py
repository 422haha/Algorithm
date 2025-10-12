vowels = ['a', 'e', 'i', 'o', 'u']
res = 0

for _ in range(int(input())):
    word = input()
    res = 0
    for i in word:
        if i in vowels:
            res += 1
    print(f"The number of vowels in {word} is {res}.")