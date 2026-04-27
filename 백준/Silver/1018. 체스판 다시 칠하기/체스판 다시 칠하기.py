n, m = map(int, input().split())
board = [input() for _ in range(n)]
cases = []

for i in range(n - 7):
    for j in range(m - 7):
        black = 0
        white = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        black += 1
                    if board[a][b] != 'W':
                        white += 1
                else:
                    if board[a][b] != 'W':
                        black += 1
                    if board[a][b] != 'B':
                        white += 1
        cases.append(black)
        cases.append(white)

print(min(cases))