# day8 ram_optimizer 

ram_usage = [2, 4, 1, 8, 3]


ram_usage. append(6)


total_ram = sum(ram_usage)
print(f"total ram usage: {total_ram} GB")

if total_ram > 16:
    print("System Overloaded!")

else:
    print("System Stable")

ram_usage. sort()
print("lowest to highest:",ram_usage)

