# Challenge 4 - File I/O: File Stats
# Read a file and display total lines, total words, and the longest line


with open("employees.txt", "r") as rf:
    content = rf.readlines()
    print(len(content))

    total_words = 0
    longest_line = ""

    for line in content:
        words = line.split()
        total_words += len(words)
        if len(line) > len(longest_line):
            longest_line = line

print(f"Total lines: {len(content)}")
print(f"Total words: {total_words}")
print(f"Longest line: {longest_line}")