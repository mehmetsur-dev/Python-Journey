# list [], .append(), .insert(), .extend(), .remove(), .pop(), .reverce(), .sort(), .sorted(), .index(), sum,max,min, 
# date 2026/13/5

courses = ["Math", "Physics", "History", "Art"]
courses_2 = ["Education, biology"]


1 # this will pick first string and print it the list starts at 0
# print(courses[0])

2 #this will pick last string in the list and print it, -1 always last string
last_item = (courses[-1])
print(last_item)

3 # adding new item to the end of the list 
# courses. append("Sport")
# print(courses)

4 # addint new item by location
# courses. insert(0, "Sport") # 0 teels python to add it first in the list
# print(courses)

# adding list to another list
# courses. extend(courses_2)
# print(courses)

# removing item from list
# courses. remove("Math")
# print(courses)

# removing and grabing removed item in another variable, new vari(popped)
# popped = courses. pop(0)
# print(popped)
# print(courses)


# Reversing the list
# courses. reverse()
# print(courses)

# Sorting the list (permanent) in alpabetic order
# courses. sort()
# print(courses)


nums = [1, 2, 3, 4, 5, 6, 7]

# sorting the list (permanent) with numbers Asending & Desending

# nums. sort() # for Asending order we leave () empty.
# print(nums) 
# nums. sort(reverse=True) # for Desending order we use reverse=True.
# print(nums)


# sortint with sorted() this will sort the list
# but will keep the orignal list too
# sorted_courses = sorted(courses)
# print(sorted_courses)


# sum, max, min
# print(sum(nums)) # this will sum all the numbers in the list
# print(max(nums)) # this will grab and print biggest number in the list 
# print(min(nums)) # this will grab and print smallesr number in the list 

# Finding and giving items lication in the list 
# print(courses. index("Math"))


# print("Art" in courses) # this will tell us if it was in the list by True or False

