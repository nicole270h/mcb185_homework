import random

def deathsave():
	failcount = 0
	successcount = 0
	revive = False
	while failcount < 3 and successcount < 3 and revive == False:
		roll = random.randint(1,20)
		if roll == 1:
			failcount +=2
		elif roll < 10:
			failcount += 1
		elif roll == 20:
			revive = True
		else: 
			successcount += 1
	if failcount >= 3:
		return "die"
	elif successcount >= 3:
		return "stable"
	elif revive == True:
		return "revive"

def probds(tries):
	diecount = 0
	stablecount = 0
	revivecount = 0
	what = 0
	for i in range(tries):
		x = deathsave()
		if x == "die":
			diecount += 1
		elif x == "stable":
			stablecount += 1
		elif x == "revive":
			revivecount += 1
	return (diecount/tries), (stablecount/tries), (revivecount/tries)

x, y, z = probds(10000)
print("death probability: " +str(x))
print("stable probability: " +str(y))
print("revive probability: " +str(z))