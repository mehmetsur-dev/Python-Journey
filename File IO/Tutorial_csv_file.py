# ============================================================
# DAY 35 - CSV MODULE EXPLAINED
# Topics: csv.reader, csv.DictReader, csv.writer, csv.DictWriter
# ============================================================

import csv
import os

# ============================================================
# SECTION 1 - CREATE A SAMPLE CSV FILE TO WORK WITH
# ============================================================

# First, let's create employees.csv so we have data to read
with open('employees.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'job'])          # header row
    writer.writerow(['Alice', '30', 'Engineer'])
    writer.writerow(['Bob', '25', 'Designer'])
    writer.writerow(['Carl', '35', 'Manager'])
    writer.writerow(['Diana', '28', 'Developer'])

print("employees.csv created!")
print()

# ============================================================
# SECTION 2 - csv.reader (rows come back as LISTS)
# ============================================================

print("--- csv.reader ---")

with open('employees.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)           # ['name', 'age', 'job'] then ['Alice', '30', 'Engineer'] etc.
        # Access by index:
        # row[0] = name
        # row[1] = age
        # row[2] = job

print()

# ============================================================
# SECTION 3 - csv.DictReader (rows come back as DICTS)
# ============================================================

print("--- csv.DictReader ---")

with open('employees.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)   # first row is automatically used as keys
    for row in reader:
        print(row)               # {'name': 'Alice', 'age': '30', 'job': 'Engineer'}
        # Access by column name:
        # row['name']
        # row['age']
        # row['job']

print()

# ============================================================
# SECTION 4 - csv.writer (write rows as LISTS)
# ============================================================

print("--- csv.writer ---")

with open('output_writer.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(['name', 'age', 'job'])           # writerow = ONE row
    writer.writerows([                                 # writerows = MULTIPLE rows at once
        ['Alice', '30', 'Engineer'],
        ['Bob', '25', 'Designer'],
        ['Carl', '35', 'Manager'],
    ])

print("output_writer.csv created!")
print()

# ============================================================
# SECTION 5 - csv.DictWriter (write rows as DICTS)
# ============================================================

print("--- csv.DictWriter ---")

fieldnames = ['name', 'age', 'job']   # you must define the field names first

with open('output_dictwriter.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()              # writeheader() writes the header row automatically
    writer.writerow({'name': 'Alice', 'age': '30', 'job': 'Engineer'})
    writer.writerow({'name': 'Bob',   'age': '25', 'job': 'Designer'})
    writer.writerow({'name': 'Carl',  'age': '35', 'job': 'Manager'})

print("output_dictwriter.csv created!")
print()

# ============================================================
# SECTION 6 - CUSTOM DELIMITER
# ============================================================

print("--- custom delimiter ---")

# Write with dash (-) as separator instead of comma
with open('output_dashes.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='-')
    writer.writerow(['name', 'age', 'job'])
    writer.writerow(['Alice', '30', 'Engineer'])

# Read it back with same delimiter
with open('output_dashes.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter='-')
    for row in reader:
        print(row)

print()

# ============================================================
# SECTION 7 - READ AND WRITE TOGETHER (copy + transform)
# ============================================================

print("--- read + write together ---")

# Read employees.csv and write a new file with only name and job (skip age)
with open('employees.csv', 'r', newline='') as read_file:
    with open('name_and_job.csv', 'w', newline='') as write_file:

        reader = csv.DictReader(read_file)
        writer = csv.DictWriter(write_file, fieldnames=['name', 'job'])

        writer.writeheader()
        for row in reader:
            writer.writerow({'name': row['name'], 'job': row['job']})

print("name_and_job.csv created!")
print()

# ============================================================
# GOLDEN RULES - READ THESE!
# ============================================================

# 1. Always use newline='' when opening CSV files
#    Without it: extra blank lines appear between rows on Windows

# 2. csv.reader / csv.writer      --> rows are LISTS  --> use index:  row[0]
#    csv.DictReader / DictWriter  --> rows are DICTS  --> use name:   row['name']

# 3. writerow()  = one row at a time
#    writerows() = multiple rows at once (pass a list of lists)

# 4. writeheader() only exists on DictWriter, not on regular writer

# 5. DictReader skips the header row automatically (uses it as keys)
#    Regular reader does NOT skip it - first row will be ['name', 'age', 'job']

print("All done! Check your folder for the new .csv files.")