a = input()
lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in lst:
    a = a.replace(i, '*')

print(len(a))