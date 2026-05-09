#day8 challenge2


dna_samples = [120, 500, 240, 750, 120, 330]

dna_samples. append(410)

dna_samples. remove(120)
dna_samples. remove(500)


total_count = len(dna_samples)
print(f"Samples left: {total_count}")

average_lenght = sum(dna_samples) / total_count
print(f"Average DNA lenght: {average_lenght}")

dna_samples. sort()
print("sorted samples:", dna_samples)