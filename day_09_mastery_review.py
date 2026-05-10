# Developer: Mehmet Sur 
#The Portfolio Optimizer


trade_prices = [2600, -50, 2100, 0, 1800, 2450, -10, 2750]

valid_trades = [price for price in trade_prices if price > 0]

valid_trades. sort()

for trade in valid_trades:
    
    if trade > 2500:
        print(f"High Value Trade: {trade}")

    elif trade >= 2000:
        print(f"Standard Trade: {trade}")

    else:
        print(f"Low Entry Trade: {trade}")

print("-" * 20)
print(f"Total Portfolio Value: {sum(valid_trades)}")
print(f"Highest Trade Found: {max(valid_trades)}")