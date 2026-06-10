# ============================================================
# DAY 35 - CSV MODULE CHALLENGES
# Topics: csv.reader, csv.DictReader, csv.writer, csv.DictWriter
# Challenges: write, read by index, read by name, DictWriter, filter + write
# ============================================================

import csv

# with open("students.csv", "w", newline='') as wf:
#     writer = csv.writer(wf)
#     writer.writerow(['name', 'grade', 'city'])
#     writer.writerows([
#         ['Jon', 'Arts', 'NYC'],
#         ['Alice', 'Software', 'Berlin'], 
#         ['Mehmet', 'Python', 'kuttenberg'],
#     ])

with open('students.csv', 'r', newline='') as rf:
    reader = csv.reader(rf)

    next(reader)

    for row in reader:
        print(f'{row[0]} - {row[2]}')


with open("students.csv", "r", newline='') as rf:
    reader = csv.DictReader(rf)

    for row in reader:
        print(f'{row["name"]} - {row["city"]}')


fieldnames = ['product', 'price', 'stock']

# with open("products.csv", "w", newline='') as wf:
#     writer = csv.DictWriter(wf, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'product': 'Catnip', 'price': 5, 'stock': 500})
#     writer.writerow({'product': 'Bow', 'price': 300, 'stock': 40})
#     writer.writerow({'product': 'Rope', 'price': 8, 'stock': 200})
fieldnames = ['product', 'price', 'stock']

with open('products.csv', 'r', newline='') as rf:
    with open('expensive.csv', 'w', newline='') as wf:

        reader = csv.DictReader(rf)
        writer = csv.DictWriter(wf, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            if int(row['price']) > 6:
                writer.writerow(row)