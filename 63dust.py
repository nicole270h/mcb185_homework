import sys
import mcb185
import gzip
import math
# enter python3 63dust.py ecolii.fna.gz 20 1.4

def entropy(a,c,t,g):
	if a != 0:
		pax = -(a/(a+c+t+g))*(math.log2(a/(a+c+t+g)))
	else:
		pax = 0
	if c != 0:
		pcx = -(c/(a+c+t+g))*(math.log2(c/(a+c+t+g)))
	else:
		pcx = 0
	if t != 0:
		ptx = -(t/(a+c+t+g))*(math.log2(t/(a+c+t+g)))
	else:
		ptx = 0
	if g != 0:
		pgx = -(g/(a+c+t+g))*(math.log2(g/(a+c+t+g)))
	else:
		pgx = 0
	shannon = pax + pcx + ptx + pgx
	return shannon


windowsize = int(sys.argv[2])
ethres = float(sys.argv[3])


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seqout = list(seq)
	for i in range(len(seq)-windowsize+1):
		minilist = seq[i:i+windowsize]
		acount = minilist.count("A")
		ccount = minilist.count("C")
		tcount = minilist.count("T")
		gcount = minilist.count("G")
		if entropy(acount, ccount, tcount, gcount) < ethres:
			for j in range(i, i+windowsize):
				seqout[j] = "N"
	seq = "".join(seqout)
	print(defline)
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])


"""
		if entropy(acount, ccount, tcount, gcount) > ethres:
			for j in range(i, i+windowsize):
				list[j] = "N"
print(list[:60])
"""
		

"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	list = []
	print(windowsize)
	print(ethres)
"""

"""
	for i in range(len(seq)-windowsize):
		list = list.append(seq[i])
		acount = [i:i+w]
		ccount = 
		tcount = 
		gcount = 
	print(name)
"""