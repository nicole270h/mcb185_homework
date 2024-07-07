seq = "ACGTACGTGGGGGACGTACGTCCCCC"
w = 10
window = seq[:w]

ccount = window.count("C")
gcount = window.count("G")

for i in range(len(seq)-w):
	if   seq[i+w] == "C": ccount += 1
	elif seq[i+w] == "G": gcount += 1
	if   seq[i]   == "C": ccount -= 1
	elif seq[i]   == "G": gcount -= 1
	
	gccomp = (ccount+gcount)/len(seq)
	
	if ccount + gcount == 0:
		gcskew = 0
	else:
		gcskew = (gcount - ccount)/(gcount + ccount)
	
	print(f"{i}\t{gccomp:.3f}\t{gcskew:.3f}")


