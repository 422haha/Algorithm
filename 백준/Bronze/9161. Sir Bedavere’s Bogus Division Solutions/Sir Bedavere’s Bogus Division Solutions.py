r = [i for i in range(100, 1000) if i%111]
for i in r:
    for j in r:
        if i%10 == j//100 and i*(j%100) == (i//10)*j:
            print(f"{i} / {j} = {i//10} / {j%100}")