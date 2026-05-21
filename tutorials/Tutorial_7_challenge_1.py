# Tutorial 7 - challenge
# Mehmet - Day 17


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num == 5:
        print('Skipped')
        continue
    if num == 9:
        print('stopped')
        break
    print(num)