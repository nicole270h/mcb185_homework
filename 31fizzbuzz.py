j=k=l=1
for i in range (1,101):
	ix=i
	if j == 3:
		j=0
		ix = "Fizz"
	else:
		j=j+1
	
	if k == 5:
		k=0
		ix = "Buzz"
	else:
		k=k+1
	if l == 15:
		l=0
		ix = "FizzBuzz"
	else:
		l=l+1
	print(ix)