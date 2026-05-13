# Day 12 Mastery: Lists, Loops, and Logic
# Date: 2026-05-13
# Goal: Consolidate Tutorial 4 concepts for GitHub portfolio

evidence = ["fingerprint", "Laptop", "USB Drive", "Fiber"]
more_evidence = ["Footprint", "Fiber"]
last_collected = []

evidence. append("Blood Sample")
#print(evidence)

evidence. insert(0, "Note")
#print(evidence)

evidence. extend(more_evidence)


evidence. remove("Laptop")
#print(evidence)

last_collected = evidence. pop(-2)
print(last_collected)


sorted_evidence = sorted(evidence)
print(sorted_evidence)


evidence. sort(reverse=True)


for index, item in enumerate(evidence, start=101):
    print(index, item)

final_list = " -- ". join(evidence)
print(final_list)