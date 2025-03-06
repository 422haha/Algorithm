n = int(input())
print(chr((n-1)%8+ord('a'))+str((n-1)//8+1))