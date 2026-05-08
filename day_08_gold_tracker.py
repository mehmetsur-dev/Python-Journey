# day8 challenge3

gold_prices = [2350, 2345, 2360, 2352]

gold_prices. append(2348)

total_prices = len(gold_prices)
print(f"Prices collected: {total_prices}")

print(f"Highest price: {max(gold_prices)}")
print(f"Lowest price: {min(gold_prices)}")

gold_prices. sort(reverse=True)
print("highes to lowest:", gold_prices)

gold_prices. remove(2345)
print("Final list after cleaning:", gold_prices)