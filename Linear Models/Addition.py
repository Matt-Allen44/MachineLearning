from sklearn import linear_model
from random import randint

#Experiment to see if we can teach a computer addition, through machine learning
clf = linear_model.LinearRegression(fit_intercept=True, normalize=False,copy_X=True,n_jobs=1)

#Number of pieces of training data
#dataDepth = 1000; 
#print "Number of pieces of training data: ", dataDepth
#raw_input("Press enter to confirm execution...")

#This attempt does not work, I believe it comes down to an error in my looping
#as the data set I generate is not useful
#Load some basics sums, format: a,b for sum a+b
#values = [0] * dataDepth;

#Load the results of the sums above, eg. a+b
#sums = [0] * dataDepth;

#for i in range(0, dataDepth):
#	for i2 in range(0, dataDepth):
#		values[i] = [i,i2] 
#		sums[i] = i+i2

#Values are in the format [a,b]
#Sums are in the format [a+b]

values = [[1,1],[0,70],[3,2]]
sums = [2,70,5]

clf.fit(values, sums)

correctSums = int(0);
lookupRange = 100000

for i in range(0,lookupRange):
	num1 = randint(lookupRange*-1,lookupRange)
	num2 = randint(lookupRange*-1,lookupRange)
	if (abs(num1+num2 - clf.predict([[num1, num2]])) < 0.001)[0]:
		correctSums = correctSums+1

	#print "%f = %f, %r" % (clf.predict([[num1, num2]]) , num1 + num2, (abs(num1+num2 - clf.predict([[num1, num2]])) < 0.001)[0])

incorrectSums = lookupRange-correctSums
print "Correct Sums: %i" % correctSums
print "Incorrect Sums: %i" % incorrectSums
print "Accuracy: %i" % (correctSums/lookupRange)