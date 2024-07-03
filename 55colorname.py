import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

with open(colorfile) as fp:
	mindist = 100000
	for line in fp:
		words = line.split()
		red, green, blue = words[2].split(",")
		taxicab = abs(R-int(red)) + abs(G-int(green) + abs(B-int(blue)))
		if mindist > taxicab: 
			mindist = taxicab
			mincolor = words[0]
	print (mincolor)
		