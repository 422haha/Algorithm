vowels = set('aeiouAEIOU')

while True:
    s = input()
    if s == '#':
        break
    print(sum(1 for c in s if c in vowels))
