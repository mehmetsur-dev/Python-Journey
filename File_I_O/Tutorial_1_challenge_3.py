# Challenge 3 - File I/O: Copy with Filter
# Read a file, filter out lines containing a user-specified word,
# write results to a new file


word = input("Enter word to filter: ")

with open('employees.txt', 'r') as rf:
    with open('filtered.txt', 'w') as wf:
        for line in rf:
            if word not in line:
                wf.write(line)