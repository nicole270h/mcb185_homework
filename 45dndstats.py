import random
# maximum and minimum functions
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
		
		
# below is for the 3D6 scenario
def one(iterations):
	total = 0
	sum = 0
	for i in range(iterations):
		a = random.randint(1,6)
		b = random.randint(1,6)
		c = random.randint(1,6)
		sum += a + b + c
		total += 1
	return (sum/total)
	
print("average for 3D6 is " + str(one(10000)))


# below is for the 3D6r1 scenario
def two(iterations):
	total = 0
	sum = 0
	for i in range(iterations):
		a = random.randint(1,6)
		b = random.randint(1,6)
		c = random.randint(1,6)
		while a == 1:
			a = random.randint(1,6)
		while b == 1:
			b = random.randint(1,6)
		while c == 1:
			c = random.randint(1,6)
		sum += a + b + c
		total += 1
	return (sum/total)

print("average for 3D6r1 is " + str(two(10000)))


# below is for the 3D6x2 scenario
def three(iterations):
	total = 0
	sum = 0
	for i in range(iterations):
		a1 = random.randint(1,6)
		a2 = random.randint(1,6)
		amax = max2(a1,a2)
		b1 = random.randint(1,6)
		b2 = random.randint(1,6)
		bmax = max2(b1,b2)
		c1 = random.randint(1,6)
		c2 = random.randint(1,6)
		cmax = max2(c1,c2)
		sum += amax + bmax + cmax
		total += 1
	return (sum/total)

print("average for 3D6x2 is " + str(three(10000)))


# below is for the 4D6d1 scenario
def four(iterations):
	total = 0
	sum = 0
	for i in range(iterations):
		a = random.randint(1,6)
		b = random.randint(1,6)
		c = random.randint(1,6)
		d = random.randint(1,6)
		sum += a + b + c + d - min2(min2(a,b), min2(c,d))
		total += 1
	return (sum/total)
	
print("average for 4D6d1 is " + str(four(10000)))
		
