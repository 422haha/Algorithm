import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dct = {}

for i in range(1, 1+n):
    j = sys.stdin.readline().rstrip()
    dct[j] = i
    dct[i] = j

for i in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isalpha():
        print(dct[quiz])
    else:
        print(dct[int(quiz)])