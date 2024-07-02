import math
import random

inside = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	dist = math.sqrt(x**2+y**2)
	total +=1
	if dist < 1:
		inside +=1
	print(4*inside/total)