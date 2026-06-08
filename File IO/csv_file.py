# Day 33 | CSV Module | Challenges 1-4 | Mehmet Sur | 07.06.2026


import csv

with open("employees.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["name", "department", "salary"])
    csv_writer.writerow(["Mehmet", "Python", 100000])
    csv_writer.writerow(["Ali", "Java", 200000])
    csv_writer.writerow(["John", "Math", 50000])
    csv_writer.writerow(["Clara", "C", 120000])
    csv_writer.writerow(["Lana", "IT", 80000])


with open("employees.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip header
    for line in csv_reader:
        print(f"Name: {line[0]} | Department: {line[1]} | Salary: {line[2]}")


with open("employees.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        if int(line["salary"]) > 4500:
            print(line)