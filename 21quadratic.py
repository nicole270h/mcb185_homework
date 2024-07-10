import math
def quadratic(a,b,c):
	if (pow(b,2)-(4*a*c))>=0:
		x1 = (-b+(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
		x2 = (-b-(math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
		return x1, x2
	else:
		x1 = x2 = "not applicable"
		return x1, x2

# above: the function
# below: 3 examples of the function executed
	
print("for the formula x^2+7x+12:")	
first, second = quadratic(1,7,12)
if first == second:
	print("roots are both " + str(first))
else:
	print("roots are " + str(first) + " and " + str(second))
	
	
print("for the formula x^2+2x+1:")	
first, second = quadratic(1,2,1)
if first == second:
	print("roots are both " + str(first))
else:
	print("roots are " + str(first) + " and " + str(second))
	
	
print("for the formula 5x^2+2x+1:")	
first, second = quadratic(5,2,1)
if first == second:
	print("roots are both " + str(first))
else:
	print("roots are " + str(first) + " and " + str(second))