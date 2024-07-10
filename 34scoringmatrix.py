alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

"""
for i in range (0, 5):
	for j in range (0,5):
		if i==j==0:
			print(end="   ")
		elif i==j:
			print(match, end=" ")
		else:
			print(mismatch, end=" ")
	print(" ")
"""
for i in range (0, 5):
	for j in range (0,5):
		if i==j==0:
			print(end="    ")
		elif i==0:
			print(alphabet[j-1],end="  ")
		elif j==0:
			print(alphabet[i-1],end="  ")
		elif i==j:
			print(match, end=" ")
		else:
			print(mismatch, end=" ")
	print("")
