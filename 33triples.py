import math
limit = 100
for i in range(0, limit):
    for j in range(i+1, limit):
        ix = i+1
        jx = j+1
        c = math.sqrt(ix**2 + jx**2)
        if c%1 == 0:
        	print(ix, jx, int(c))