import sys
text = sys.stdin.readline()
num = 0
for i in text:
    if i in ['A', 'B', 'C']:
        num += 3
    elif i in ['D', 'E', 'F']:
        num += 4
    elif i in ['G', 'H', 'I']:
        num += 5
    elif i in ['J', 'K', 'L']:
        num += 6
    elif i in ['M', 'N', 'O']:
        num += 7
    elif i in ['P', 'Q', 'R', 'S']:
        num += 8
    elif i in ['T', 'U', 'V']:
        num += 9
    elif i in ['W', 'X', 'Y', 'Z']:
        num += 10
print(num)