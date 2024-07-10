def factorial(a):
	fact = 1
	for i in range(1,a+1):
		fact = fact*i
	return fact

def nk(n,k):
	if k>n:
		return "not applicable"
	else:
		ans = factorial(n)/(factorial(k)*factorial(n-k))
		return ans
	
print(nk(4,2))
print(nk(5,1))
print(nk(4,4))
print(nk(3,5))