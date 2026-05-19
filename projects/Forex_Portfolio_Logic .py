# Day 14: Python Mastery Project
# Integrating Tutorials 1, 2, 3, and 4
# Focus: Forex Portfolio Logic

greeting = "Hello"
name = "Mehmet"
pair = "XAU/USD"

# Using f-string for a clean welcome message
message = f"{greeting}, {name}. Welcome to your {pair} tracker!"
print(message)

# String manipulation: Checking the length and case
print(f"Tracking Pair: {pair.upper()}")
print(f"Character Count: {len(pair)}")
print("-" * 30)


# Simulating a web input as a string
balance_str = "15000"
gold_price = 2300

# Converting string to int to perform math
balance_int = int(balance_str)

# Using Floor Division and Modulus
units_can_buy = balance_int // gold_price
remaining_cash = balance_int % gold_price

print(f"Total Balance: {balance_int}")
print(f"Units of Gold possible: {units_can_buy}")
print(f"Cash leftover: {remaining_cash}")
print("-" * 30)


watchlist = ["EUR/USD", "GBP/USD", "USD/JPY"]

# Adding and removing items
watchlist.append("BTC/USD")
watchlist.insert(0, "ETH/USD")
watchlist.remove("USD/JPY")

# Sorting the list
watchlist.sort()

print("Current Watchlist:")
# Using enumerate to loop with numbers
for index, item in enumerate(watchlist, start=1):
    print(index, item)
print("-" * 30)


# Comparing your list with a "Broker 2" list
broker_1_set = set(watchlist)
broker_2_set = {"EUR/USD", "XAU/USD", "TRY/USD"}

# Finding common items (Intersection)
common = broker_1_set.intersection(broker_2_set)

# Finding all unique items (Union)
all_assets = broker_1_set.union(broker_2_set)

print(f"Common items on both brokers: {common}")
print(f"Total unique assets available: {all_assets}")
