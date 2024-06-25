import sys


def cal(s1, s2):
    if len(s1) != len(s2):
        return False

    if s1[0] != s2[0] or s1[-1] != s2[-1]:
        return False

    vowels = {'a', 'e', 'i', 'o', 'u'}
    cnt_s1 = {}
    cnt_s2 = {}

    temp_s1 = []
    temp_s2 = []

    for i in range(len(s1)):
        char_s1 = s1[i]
        char_s2 = s2[i]

        cnt_s1[char_s1] = cnt_s1.get(char_s1, 0) + 1
        cnt_s2[char_s2] = cnt_s2.get(char_s2, 0) + 1

        if char_s1 not in vowels:
            temp_s1.append(char_s1)
        if char_s2 not in vowels:
            temp_s2.append(char_s2)

    if cnt_s1 != cnt_s2:
        return False

    return ''.join(temp_s1) == ''.join(temp_s2)


n = int(sys.stdin.readline().rstrip())
s1 = str(sys.stdin.readline().rstrip())
s2 = str(sys.stdin.readline().rstrip())

if not cal(s1, s2):
    print('NO')
else:
    print('YES')