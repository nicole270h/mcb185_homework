import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

samecount = 0
for i in range(trials):
	samebday = False
	bdaysum = []
	for j in range(people):
		x = random.randint(1, days)
		bdaysum.append(x)
	bdaysum.sort()
	for k in range(len(bdaysum)-1):
		if bdaysum[k] == bdaysum [k+1]:
			samebday = True
	if samebday == True:
		samecount += 1
print(samecount/trials)
		