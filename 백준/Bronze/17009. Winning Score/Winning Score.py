apple = 0
banana = 0

for i in range(3, 0, -1):
    apple += int(input())*i
for i in range(3, 0, -1):
    banana += int(input())*i

if apple > banana:
    print('A')
elif apple < banana:
    print('B')
else:
    print('T')