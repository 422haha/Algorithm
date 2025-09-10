n = int(input())
m = int(input())
adjectives = [input() for _ in range(n)]
nouns = [input() for _ in range(m)]

for adj in adjectives:
    for noun in nouns:
        print(f"{adj} as {noun}")