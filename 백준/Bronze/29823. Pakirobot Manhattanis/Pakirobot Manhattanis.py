_ = int(input())
lst = list(map(str, input()))
n, w, e, s = map(lst.count,'NWES')
print(abs(n-s)+abs(w-e))