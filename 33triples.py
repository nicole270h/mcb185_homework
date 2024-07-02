import math

limit = 100
for a in range(1, limit+1):
    for b in range(a+1, limit+1):
        c = math.sqrt(a**2 + b**2)
        if c%1 == 0:
        	print(a, b, int(c))