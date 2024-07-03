import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

with gzip.open(gffpath, "rt") as fp:
	for line in fp:	
		if line[0] == "#": continue
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])
		end = int(words[4])
		lengths.append(end - beg + 1)



print("Count: "+ str(len(lengths)))	

lengths.sort()
print("Min: " + str(lengths[0]))
print("Max: " + str(lengths[-1]))

total = 0
for val in lengths: total += val
mean = total/len(lengths)
print(f"Mean: {mean:.0f}")


deviationsum = 0
for val in lengths: deviationsum += (val-mean)**2
stdev = math.sqrt(deviationsum/len(lengths))
print(f"Standard deviation: {stdev:.0f}")



if len(lengths)%2 == 0:
	median = ((lengths[int((len(lengths)/2)-1)]+lengths[int((len(lengths)/2))])/2)
else:
	median = lengths[int((len(lengths)+1)/2)]

print(f"Median: {median:.0f}")
