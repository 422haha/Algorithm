while True:
    n = int(input())
    if n == 0:
        break
    covered_numbers = set()
    
    for _ in range(n):
        ticket = list(map(int, input().split()))
        for num in ticket:
            if 1 <= num <= 49:
                covered_numbers.add(num)
    
    if len(covered_numbers) == 49:
        print("Yes")
    else:
        print("No")