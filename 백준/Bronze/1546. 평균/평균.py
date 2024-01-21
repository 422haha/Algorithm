import sys
n = int(sys.stdin.readline())
a = sys.stdin.readline()

score = [int(i) for i in a.split(' ')]
max_score = max(score)
fake_mean = sum(score)/n/max_score*100

print(fake_mean)