s = input()
lst = 'aeiou'

cnt = 0
for i in lst:
    cnt += s.count(i)
print(cnt)