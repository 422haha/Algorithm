score = {
    '.': 0, 'K': 0, 'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9,
    'k': 0, 'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9
}

print(sum([sum([score[i] for i in input()]) for _ in range(8)]))
