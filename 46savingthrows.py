import random

def min2(a,b):
	if a>=b:
		return b
	else:
		return a

def max2(a,b):
	if a>=b:
		return a
	else:
		return b
		
#savingthrow returns true=success and false=failure
#the adv parameter in savingthrow is as follows:
# 0 normal, 1 advantage, -1 disadvantage
def savingthrow(dc, adv):
	xd20 = random.randint(1,20)
	yd20 = random.randint(1,20)
	badd20 = min2(xd20, yd20)
	if adv == 1:
		d20 = max2(xd20, yd20)
	if adv == 0:
		d20 = xd20
	if adv == -1:
		d20 = min2(xd20, yd20)
	if d20 >= dc:
		return True
	else:
		return False
		
#probability of saving throw success under parameters
def probst(diffclass, advant, num):
	success = 0
	for i in range(num):
		if savingthrow(diffclass, advant) is True:
			success += 1
	return (success/num)

#variables for the table
dc1 = 5
dc2 = 10
dc3 = 15
tries = 10000


#making the table lmao
print (" ", "N", "D", "A", sep="\t")
print (dc1, probst(dc1, 0, tries), probst(dc1, -1, tries), probst(dc1, 1, tries), sep= "\t")
print (dc2, probst(dc2, 0, tries), probst(dc2, -1, tries), probst(dc2, 1, tries), sep= "\t")
print (dc3, probst(dc3, 0, tries), probst(dc3, -1, tries), probst(dc3, 1, tries), sep= "\t")