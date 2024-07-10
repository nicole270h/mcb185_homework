import tools

seq = "ACGTACGTGGGGGACGTACGTCCCCC"
w = 10
for i in range(len(seq)-w+1):
	s = seq[i:i+w]
	print(i, tools.gc_comp(s), tools.gc_skew(s))