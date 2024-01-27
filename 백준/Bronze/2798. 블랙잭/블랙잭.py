n, m = map(int, input().split())
card = list(map(int, input().split()))
max_card = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = card[i] + card[j] + card[k]
            if card_sum > m:
                continue
            else:
                if card_sum >= max_card:
                    max_card = card_sum
print(max_card)