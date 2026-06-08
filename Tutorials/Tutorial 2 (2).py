# Tutorial_2: Strings

messege = "Hello World"

# [0:5] this tells python to get only Hello word
print(messege[0:5])

# len() counts every character, including letters, numbers, spaces, and punctuation.
# 'hello world' witch is (11), 10 letter, 1 space, =11 
print(len(messege))

# .lower() this will make 'HELLO WORLD' lower case 
print(messege. lower())

# .upper() this will make 'hello world' upper case
print(messege. upper())

# .count() this tels us how many (o) are there in "Hello World" we can also do hole word
print(messege. count("o"))

#this will find the word and tell us its index number, if the word was not there
#it will show -1
print(messege. find("World"))


# .replace("orignal", "new word")  this will replace the orignal text with new one 
messege = messege. replace("World", "Cat")
print(messege)