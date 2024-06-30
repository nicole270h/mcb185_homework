import math
def entropy(a,c,t,g):
	if a != 0 and c !=0 and t != 0 and g != 0:
		pa = a/(a+c+t+g)
		pc = c/(a+c+t+g)
		pt = t/(a+c+t+g)
		pg = g/(a+c+t+g)
		shannon = -pa*(math.log2(pa))-pc*(math.log2(pc))-pt*(math.log2(pt))-pg*(math.log2(pg))
		return shannon
	else:
		return "not applicable"
		
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
	