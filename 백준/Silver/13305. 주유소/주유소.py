num_cities = int(input())
road_lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
total_cost = 0

for i in range(num_cities - 1):
    if min_price > prices[i]:
        min_price = prices[i]
    total_cost += min_price * road_lengths[i]

print(total_cost)