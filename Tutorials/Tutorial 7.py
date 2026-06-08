# for loop 

nums = [1, 2, 3, 4, 5]


# {for} loop important keywords (break), (continue)
# The ((break)) keyword immediately stops the entire loop,
# even if there are items left in the list.
# for num in nums:
#     if num == 3:
#         print('Found!') # # Triggers when num is 3 
#         break           # # Exits the loop completely and it will not print 3 
#     print(num)
    


print('o---------------------------------------o')

# The ((continue)) keyword skips the current iteration 
# and immediately jumps to the next item in the sequence.
# It does not stop the whole loop.
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)



print('o--------------------------------------o')

# Outer loop runs through numbers, inner loop runs through characters
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)


print('o--------------------------------------o')

# # (range) Counts from 0 up to (but not including) the stop number (10).
# for i in range(10):
#     print(i)

# # Counts from your specific start number
# # up to (but not including) the stop number.
# for i in range(1, 11):
#     print(i)