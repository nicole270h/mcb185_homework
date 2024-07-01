import math
def entropy(a,c,t,g):
	pa = a/(a+c+t+g)
	pc = c/(a+c+t+g)
	pt = t/(a+c+t+g)
	pg = g/(a+c+t+g)
	if a != 0:
		pax = -pa*(math.log2(pa))
	else:
		pax = 0
	if c != 0:
		pcx = -pc*(math.log2(pc))
	else:
		pcx = 0
	if t != 0:
		ptx = -pt*(math.log2(pt))
	else:
		ptx = 0
	if g != 0:
		pgx = -pg*(math.log2(pg))
	else:
		pgx = 0
	shannon = pax + pcx + ptx + pgx
	return shannon
		
aden = 2
cyto = 2
guan = 2
thym = 2
shan = entropy(aden, cyto, guan, thym)
print ("Shannon entropy is " + str(shan))

aden = 17
cyto = 16
guan = 17
thym = 17
shan = entropy(aden, cyto, guan, thym)
print ("Shannon entropy is " + str(shan))

aden = 5
cyto = 1
guan = 19
thym = 1
shan = entropy(aden, cyto, guan, thym)
print ("Shannon entropy is " + str(shan))

aden = 0
cyto = 0
guan = 1
thym = 3
shan = entropy(aden, cyto, guan, thym)
print ("Shannon entropy is " + str(shan))
	