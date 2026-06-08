# ============================================================
# FILE I/O - TUTORIAL 1 NOTES
# Corey Schafer - File Objects: Reading and Writing to Files
# Day 30 - Mehmet Sur
# ============================================================


# ------------------------------------------------------------
# 1. OPENING A FILE - open()
# ------------------------------------------------------------
# open(filename, mode)
# Always use 'with' statement — it automatically closes the file!

# with open('filename.txt', 'mode') as f:
#     do something with f


# ------------------------------------------------------------
# 2. FILE MODES
# ------------------------------------------------------------
# 'r'  → read only (default)
# 'w'  → write (creates file if not exists, DELETES content if exists!)
# 'a'  → append (adds to end of file, does NOT delete existing content)
# 'r+' → read AND write


# ------------------------------------------------------------
# 3. READING A FILE
# ------------------------------------------------------------
# with open('employees.txt', 'r') as f:

#     f.read()         → reads entire file as one string
#     f.readline()     → reads one line at a time
#     f.readlines()    → reads all lines, returns a LIST


# ------------------------------------------------------------
# 4. .seek()
# ------------------------------------------------------------
# After reading, the cursor is at the END of the file.
# .seek(0) moves the cursor back to the BEGINNING.

# with open('employees.txt', 'r') as f:
#     f.read()    # cursor is now at the end
#     f.seek(0)   # move cursor back to start
#     f.read()    # now you can read again!


# ------------------------------------------------------------
# 5. WRITING TO A FILE
# ------------------------------------------------------------
# with open('employees.txt', 'w') as f:
#     f.write('Some text\n')   # \n = new line
# WARNING: 'w' mode will DELETE all existing content first!


# ------------------------------------------------------------
# 6. APPENDING TO A FILE
# ------------------------------------------------------------
# with open('employees.txt', 'a') as f:
#     f.write('New line added\n')
# 'a' mode NEVER deletes existing content, just adds to the end.


# ------------------------------------------------------------
# 7. COPYING A FILE
# ------------------------------------------------------------
# with open('original.txt', 'r') as rf:
#     with open('copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


# ------------------------------------------------------------
# 8. FOR LOOP & WHILE LOOP WITH FILES
# ------------------------------------------------------------

# FOR LOOP — iterates line by line:
# with open('employees.txt', 'r') as f:
#     for line in f:
#         print(line, end='')  # end='' avoids double newlines

# WHILE LOOP — reads chunk by chunk (useful for large files):
# with open('employees.txt', 'r') as f:
#     while True:
#         chunk = f.read(100)   # read 100 characters at a time
#         if not chunk:
#             break
#         print(chunk, end='')


# ------------------------------------------------------------
# 9. end='' TRICK
# ------------------------------------------------------------
# Each line in a file already has \n at the end.
# print() also adds \n by default.
# So you get double spacing!
# Fix: use print(line, end='') to suppress print's extra newline.


# ============================================================
# QUICK REFERENCE
# ============================================================
# open(file, 'r')          → read
# open(file, 'w')          → write (overwrites!)
# open(file, 'a')          → append
# f.read()                 → entire file as string
# f.readline()             → one line
# f.readlines()            → list of all lines
# f.write('text')          → write string to file
# f.seek(0)                → move cursor to beginning
# for line in f            → loop line by line
# print(line, end='')      → no double newline
# ============================================================