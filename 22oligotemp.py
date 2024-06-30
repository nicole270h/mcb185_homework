def oligotemp (a,c,g,t):
	if (a+c+g+t) <= 13:
		Tm = (a+t)*2 + (g+c)*4
	else:
		Tm = 64.9 + 41*(g+c-16.4) / (a+c+g+t)
	return Tm
	
aden = 1
cyto = 4
guan = 3
thym = 2
melttemp = oligotemp(aden, cyto, guan, thym)
print ("oligo with " + str(aden) + "A, " + str(cyto) + "C, " + str(guan) + "G, " + str(thym) + "T, has a melting temp of " + str(melttemp))


aden = 2
cyto = 20
guan = 15
thym = 16
melttemp = oligotemp(aden, cyto, guan, thym)
print ("oligo with " + str(aden) + "A, " + str(cyto) + "C, " + str(guan) + "G, " + str(thym) + "T, has a melting temp of " + str(melttemp))


aden = 2
cyto = 3
guan = 3
thym = 5
melttemp = oligotemp(aden, cyto, guan, thym)
print ("oligo with " + str(aden) + "A, " + str(cyto) + "C, " + str(guan) + "G, " + str(thym) + "T, has a melting temp of " + str(melttemp))