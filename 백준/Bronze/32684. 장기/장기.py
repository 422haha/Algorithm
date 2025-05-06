weights = [13, 7, 5, 3, 3, 2]

cheok = list(map(int, input().split()))
eun = list(map(int, input().split()))

cheok_score = sum(c*w for c, w in zip(cheok, weights))
eun_score = sum(e*w for e, w in zip(eun, weights))+1.5

if cheok_score > eun_score:
    print("cocjr0208")
else:
    print("ekwoo")