



# Challenge 1 — Warm Up 🟢

import math
import random

user_input = float(input('Please enter a number: '))
print(f'You entered: {user_input}')

print(f'Square root {math.sqrt(user_input)}')

print(f'Random number between 1 and {int(user_input)}: {random.randint(1, int(user_input))}')



# Challenge 2 — Medium 🟡

from string_tools import reverse_text as rs
from string_tools import count_word as cw
from string_tools import make_uppercase as mup

user_input_1 = input('To reverse text type here: ')
print(f'Reversed text: {rs(user_input_1)}')

user_input_2 = input('To count text type here: ')
print(f'Counted Text: {cw(user_input_2)}')

user_input_3 = input('Auto uppercase type here: ')
print(f'Uppercase Text: {mup(user_input_3)}')



# Challenge 3 — Hard 🔴

from student import add_student as add
from student import remove_student as rmv
from student import show_students as sho

students = ["Mehmet", "Sur", "Nico"]

user_0 = input('Add student here: ')
add(students, user_0)
print(f'{user_0} added successfully!')

user_1 = input('Remove student here: ')
rmv(students, user_1)
print(f'{user_1} removed successfully!')

print(f'Final fixed list:')
sho(students)