t = int(input())

for i in range(t):
    coin = float(input())
    quarters = int(coin // 25)
    dimes = int((coin - quarters*25) // 10)
    nickels = int((coin - quarters*25 - dimes*10) // 5)
    pennies = int((coin - quarters*25 - dimes*10 - nickels*5) / 1)
    print(f'{quarters} {dimes} {nickels} {pennies}')