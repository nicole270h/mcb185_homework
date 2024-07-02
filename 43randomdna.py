import random
seqnum = 3
lowerbound = 50
upperbound = 60

for i in range (seqnum):
	print(f">seq-{i+1}")
	for j in range(random.randint(lowerbound,upperbound)):
		print(random.choice("ACTG"), end ="")
	print("")