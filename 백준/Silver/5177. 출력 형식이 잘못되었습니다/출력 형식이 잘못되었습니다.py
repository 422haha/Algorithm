import sys


def formalize(s):
    s = s.strip().replace(',', ';').lower()
    for c in "{[": s = s.replace(c, '(')
    for c in "}]": s = s.replace(c, ')')
    while '  ' in s: s = s.replace('  ', ' ')
    for c in "().,;:": s = s.replace(' '+c, c).replace(c+' ',c)
    return s


t = int(sys.stdin.readline().rstrip())
for tc in range(1, t+1):
    a = formalize(input())
    b = formalize(input())
    print(f"Data Set {tc}: {'not ' if a != b else ''}equal")
    print()