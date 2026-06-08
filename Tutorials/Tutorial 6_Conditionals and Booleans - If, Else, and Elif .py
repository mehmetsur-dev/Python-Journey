# if _ elif _ else _ statments .

language = 'python'

if language == 'python':
    print('language is python')

elif language == 'java':
    print('language is java')

elif language == 'javaScript':
    print('language is javaScript')

else:
    print('No match')


# boolean opration we can use with if
#  
# Using (and) requires both conditions to be True.

# Using (or) only requires at least one condition to be True.

# Using (not) just flips the Boolean value (making not False evaluate to True),
# which is perfect for checking states like if not logged_in:.

user = 'Admin'
logged_in = False

# using and 
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# using or
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# using not
if not logged_in:
    print('Please log in')
else:
    print('Welcome') 

print('---------------------------------------------')

# Object identity: is 
a = [1, 2, 3]
b = [1, 2, 3]

# when we print id of a and b its not same so (is) will not print True
# if the id was same (is) would give True 
# we can get any list or varible ID using id keyword
print(id(a))
print(id(b))


print(a == b)
print(a is b)