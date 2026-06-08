# Challenge_2

total_bill = "850"
people = "4"

# Convert both of those string inputs into integers so you can do math.
total_bill = int(total_bill)
people = int(people)


# Calculate how much each person pays using standard division.
print(total_bill / people)


# Calculate how many full dollars each person pays using floor division.
print(total_bill // people)


# Use the modulus operator (%) to find out how many dollars are "left over".
print(total_bill % people)


# Create a variable called is_even_split.
# Use a comparison operator to check if the remainder is equal to 0.
is_even_split = total_bill % people
print(is_even_split == 0)