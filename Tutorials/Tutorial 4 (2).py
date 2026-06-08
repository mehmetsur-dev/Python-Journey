# Looping Values
# date 2026/13/5

courses = ["Math", "Art", "Physics", "Biology"]

# this will print each string with new line 
# for item in courses: # in this line we can change item word whatever we want 
#     print(item)


# this will loop and add number in each line and it will start with 0 index
for index, course in enumerate(courses, start=1): # start=1 will make the number start with 1 
    print(index, course)


# this will add symbls btween each string by .join()
course_str = ' >< '. join(courses)
print(course_str)

# # We can reverse this by .split()
new_list = course_str. split(" - ")
print(new_list)

