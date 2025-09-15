cards = set()
for _ in range(51):
    cards.add(input())

suits = ['S', 'B', 'V', 'K']
for suit in suits:
    for value in range(1, 14):
        card = f"{suit} {value}"
        if card not in cards:
            print(card)
            break
    else:
        continue
    break