import sys
import math

def prime(num):
    if num == 0 or num == 1 or num ==2:
        return 2
    sq = math.ceil((math.sqrt(num)))
    for i in range(2, sq+1):
        if num % i == 0:
            return False
    return num


t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    n = int(sys.stdin.readline().rstrip())
    result = 0
    while result == 0:
        result = prime(n)
        n += 1
    print(result)