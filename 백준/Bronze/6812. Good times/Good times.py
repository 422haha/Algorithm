t = int(input())

h = t//100
m = t%100

def c(dh, dm=0):
    total_m = h*60+m+dh*60+dm
    nh = (total_m//60)%24
    nm = total_m%60
    return nh*100+nm

print(f"{t} in Ottawa")
print(f"{c(-3)} in Victoria")
print(f"{c(-2)} in Edmonton")
print(f"{c(-1)} in Winnipeg")
print(f"{t} in Toronto")
print(f"{c(1)} in Halifax")
print(f"{c(1, 30)} in St. John's")