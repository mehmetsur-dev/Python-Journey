# ============================================================
# FILE I/O - TUTORIAL 1 - CHALLENGE 1
# Topic: Writing and Reading a File
# Day 30 - Mehmet Sur
# ============================================================


# Step 1: CREATE and WRITE the file
with open('employees.txt', 'w') as wf:
    wf.write('Ali Veli - Python Developer\n')
    wf.write('Mehmet Sur - Junior Developer\n')
    wf.write('Ayse Kaya - Data Analyst\n')

# Step 2: READ and PRINT the file
with open('employees.txt', 'r') as rf:
    rf_contents = rf.read()
    print(rf_contents)
