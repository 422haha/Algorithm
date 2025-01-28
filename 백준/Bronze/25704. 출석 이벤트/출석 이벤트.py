n, p = int(input())//5, int(input())
print(max(0, p-max([0, 500, p//10, 2000, p//4][:n+1])))