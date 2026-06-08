# Dictionaries

# this called dictionary made of keys and values 
student = {"name": "john", "age": 25, "courses": ["Math", "Art"]}

# print(student["name"])

# # if we want to know all the keys in our dictionary we can use .keys()
# print(student. keys())

# # if we want all the values in our dictionary we can use .values()
# print(student. values())

# # if we want to see both keys and values we use .items()
# print(student. items())

# now how to loop in this dictionary
for key, value in student. items():
    print(key, value)


print(" ------------------ ")


# when we use .get() and the item were we looking for was missing in he dictionary
# it wont give error i will just say None
print(student. get("name"))
# here phone dose not exist in list but we did not get error thanks to .get()
print(student. get("phone")) 
# we can also change the result to anything we want None to Not Found
print(student. get("phone", "Not Found"))


# we can update the dictionary by .update() 
student. update({"name": "Jane", "age": 21})
print(student)

# we can delete a key and value in the dicitonary by using del
del student["age"]
print(student)

