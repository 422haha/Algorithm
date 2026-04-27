while True:
    n = int(input())
    if n < 0:
        break
    lst = [i for i in range(1, n) if n % i == 0]
    if sum(lst) == n:
        print(f'{n} = ', end ='')
        for idx, j in enumerate(lst):
            if idx == len(lst) - 1:
                print(j, end='')
            else:
                print(f'{j} + ', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')