def accuracy(tp, fp, tn, fn):
	acc = (tp+tn)/(tp+fp+tn+fn)
	f1 = tp/(tp+((fp+fn)/2))
	return acc, f1
	
truepos = 1
falsepos = 10
trueneg = 3
falseneg = 7
x, y = accuracy(truepos, falsepos, trueneg, falseneg)
print("accuracy is " + str(x))
print ("f1 is " + str(y))
print(" ")

truepos = 100
falsepos = 0
trueneg = 100
falseneg = 1
x, y = accuracy(truepos, falsepos, trueneg, falseneg)
print("accuracy is " + str(x))
print ("f1 is " + str(y))
print(" ")

truepos = 100
falsepos = 1
trueneg = 100
falseneg = 0
x, y = accuracy(truepos, falsepos, trueneg, falseneg)
print("accuracy is " + str(x))
print ("f1 is " + str(y))
print(" ")

truepos = 1
falsepos = 0
trueneg = 2
falseneg = 0
x, y = accuracy(truepos, falsepos, trueneg, falseneg)
print("accuracy is " + str(x))
print ("f1 is " + str(y))
print(" ")