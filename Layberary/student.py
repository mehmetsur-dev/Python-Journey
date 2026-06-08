


def add_student(students, name):
    """Adds a name to the list."""
    students.append(name)


def remove_student(students, name):
    """Removes a name from the list if it exists."""
    if name in students:
        students.remove(name)
    else:
        print(f'{name} was not found in the list.')


def show_students(students):
    """Prints all students nicely."""
    print("Student List:")
    for student in students:
        print(f'-{student}')