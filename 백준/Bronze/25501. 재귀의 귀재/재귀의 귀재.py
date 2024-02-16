import sys


def palindrome(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return palindrome(s, l+1, r-1)


t = int(sys.stdin.readline())
for tc in range(1, t+1):
    s = sys.stdin.readline().rstrip()
    cnt = 0
    print(palindrome(s, 0, len(s)-1), cnt)