import sys

t = int(sys.stdin.readline())
for tc in range(t):
    n = sys.stdin.readline().rstrip()
    result_score = 0
    score = 0
    for i in n:
        if i == 'O':
            score += 1
            result_score += score
        else:
            score = 0
    print(result_score)