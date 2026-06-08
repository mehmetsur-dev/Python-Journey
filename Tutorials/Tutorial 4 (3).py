# Tuples 

courses = ("Math", "History", "Art", "Suport")
# Tuples are basicly a list with () and we cant change it remove item
#  or add item 


# Sets
courses_2 = {"Math", "History", "Art", "Suport",}
courses_3 = {"Math", "History", "CSI", "Biology"}
# Sets are lists with {} braket and when we print it 
# if there is and dubble items in the list it will delete it 
# also it will not print in order 
print(courses_2)

print(courses_2. intersection(courses_3)) # this will show the same items in both lists 

print(courses_2. difference(courses_3)) # this will show witch item is not in list2

print(courses_2. union(courses_3)) # this will make both list in one list 

#-------------------------------------------------------------
# how we can make empty Lists, Tuples, Sets 

# Empty List
empty_list = [] 
empty_list = list() # we can do like this too with list() keyword


# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()


# Empty Sets
empty_set = {} # This is not right we cant do empty set like that 
empty_set = set()