# Day 13: Sets and Tuples Challenge
# Focus: CSI Evidence Analysis
# date : 5/14/2026

location_a_evidence = {"Fingerprint", "Shell", "Casing", "DNA Sample"}
location_b_evidence = {"DNA Sample", "Footprint", "Fiber"}

print(location_a_evidence. intersection(location_b_evidence))

print(location_a_evidence. difference(location_b_evidence))

print(location_a_evidence. union(location_b_evidence))

all_evedince = location_a_evidence. union(location_b_evidence)
immutable_evidence_log = tuple(all_evedince)

cleared_evidince = set()