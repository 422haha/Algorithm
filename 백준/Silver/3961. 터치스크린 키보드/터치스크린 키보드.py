import sys
def tuple_subtraction(t1, t2):
    return int(abs(t1[0]-t2[0])+abs(t1[1]-t2[1]))


arr1 = ['qwertyuiop', 'asdfghjkl*', 'zxcvbnm***']
arr2 = []
dct = {}
for i in range(3):
    lst = []
    for j in range(10):
        lst.append((i, j))
    arr2.append(lst)
for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        dct[arr1[i][j]] = arr2[i][j]

t = int(sys.stdin.readline())

for tc in range(1, t+1):
    alpha, n = sys.stdin.readline().split()
    lst1 = [dct[i] for i in alpha]
    lst3 = []
    for i in range(int(n)):
        lst2 = []
        sum_value = 0
        input_value = sys.stdin.readline().rstrip()
        for j in input_value:
            lst2.append(dct[j])
        for k in range(len(lst1)):
            sum_value += tuple_subtraction(lst1[k], lst2[k])
        lst3.append((input_value, sum_value))
    lst3.sort(key = lambda x : (x[1], x[0]))
    for input_value, sum_value in lst3:
        print(f"{input_value} {sum_value}")