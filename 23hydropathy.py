def hydropathy(x):
	if x == "A":
		return 1.8
	elif x == "C":
		return 2.5
	elif x == "D":
		return -3.5
	elif x == "E":
		return -3.5
	elif x == "F":
		return 2.8
	elif x == "G":
		return -0.4
	elif x == "H":
		return -3.2
	elif x == "I":
		return 4.5
	elif x == "K":
		return -3.9
	elif x == "L":
		return 3.8
	elif x == "M":
		return 1.9
	elif x == "N":
		return -3.5
	elif x == "P":
		return -4.5
	elif x == "Q":
		return -0.8
	elif x == "R":
		return -4.5
	elif x == "S":
		return -0.8
	elif x == "T":
		return -0.7
	elif x == "V":
		return 4.2
	elif x == "W":
		return -0.9
	elif x == "Y":
		return -1.3
	else:
		return "not applicable"
		
amino = "A"
num = hydropathy(amino)
print("the K-D hydrophobicity value for " + amino + " is " + str(num))

amino = "P"
num = hydropathy(amino)
print("the K-D hydrophobicity value for " + amino + " is " + str(num))

amino = "Y"
num = hydropathy(amino)
print("the K-D hydrophobicity value for " + amino + " is " + str(num))

amino = "B"
num = hydropathy(amino)
print("the K-D hydrophobicity value for " + amino + " is " + str(num))