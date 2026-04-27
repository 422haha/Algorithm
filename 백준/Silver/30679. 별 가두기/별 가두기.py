import sys


def is_capturable(n, m, arr, start_row):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    visited = set()

    r, c = start_row, 0
    d = 0

    while True:
        if (r, c, d) in visited:
            return True
        visited.add((r, c, d))

        level = arr[r][c]
        dr, dc = directions[d]

        nr = r + dr * level
        nc = c + dc * level

        if not (0 <= nr < n and 0 <= nc < m):
            return False

        r, c = nr, nc
        d = (d+1) % 4


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

capturable_rows = []

for r in range(n):
    if is_capturable(n, m, arr, r):
        capturable_rows.append(r + 1)

print(len(capturable_rows))
if capturable_rows:
    print(" ".join(map(str, capturable_rows)))