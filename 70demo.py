seq = "ACGTACGTGGGGGACGTACGTCCCCC"
count = {}
for nt in seq:
    if nt not in count: count[nt] = 0
    count[nt] += 1

print(count)
counts = {"A":"first", "C":"second", "B":"third"}
for k in sorted(counts): print(k, counts[k])