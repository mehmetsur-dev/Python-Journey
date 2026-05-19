# list methods

orders = ["Wood", "Iron", "Silk", "food"]
orders.append("Clay")  # This adds Clay to the end of the orders list

for order in orders:
    if order.startswith("W"):
        print(f"Processing {order} for the workshop")
