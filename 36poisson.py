import math

def factorial(a):
	fact = 1
	for i in range(1,a+1):
		fact = fact*i
	return fact

def poisson(n,k):
	ans = (math.pow(n,k)*math.pow(math.e,-n))/factorial(k)
	return ans


print(poisson(3,2))
print(poisson(1,2))
print(poisson(10,0))