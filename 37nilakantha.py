x=0
pi=3
for i in range(15):
	for i in range (2):
		x=x+2
		if i==0:
			pi = pi + 4/(x*(x+1)*(x+2))
		else:
			pi = pi - 4/(x*(x+1)*(x+2))
		print(pi)

	