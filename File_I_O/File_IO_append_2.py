# Challenge 2 - Activity Log
# Day 32 - File I/O Append Mode

with open("log.txt", "a") as af:
    af.write("[Run 3] User logged in\n")

with open("log.txt", "r") as rf:
    print(rf.read())