# Day 17: Python Loops Reference Guide
# Demonstrating for loops, while loops, control statements, and nesting.


#  1. For Loop Basics & Lists
print("--- 1. For Loop Basics ---")
nums = [1, 2, 3, 4, 5]  
for num in nums:  
    print(f"Current number: {num}")

#  2. Loop Control: Break
print("\n--- 2. Loop Control: Break ---")
for num in nums:  
    if num == 3:  
        print("Found 3! Breaking the loop completely.")  
        break  
    print(num)  

#  3. Loop Control: Continue
print("\n--- 3. Loop Control: Continue ---")
for num in nums:  
    if num == 3:  
        print("Found 3! Skipping this specific number.")  
        continue 
    print(num)  

#  4. Nested Loops
print("\n--- 4. Nested Loops ---")
for num in nums[:3]:  # Using first 3 numbers to keep output clean
    for letter in 'abc':  
        print(num, letter)  

#  5. Looping with range()
print("\n--- 5. Looping with range() ---")
for i in range(1, 6):  # Counts from 1 up to 5
    print(f"Range value: {i}")

# 6. Standard while Loop
print("\n--- 6. Standard While Loop ---")
x = 0  
while x < 5:  
    print(f"x is currently: {x}")  
    x += 1  # Increments to prevent infinite loop

# 7. Intentional Infinite Loop with Break
print("\n--- 7. Intentional Infinite Loop with Break ---")
count = 0  
while True:  
    if count == 3:  
        print("Hit 3! Triggering emergency break exit.")  
        break  
    print(count)  
    count += 1  