from sklearn import linear_model

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
values = [[1,1],[0,70],[3,2],[4,7]]
sums = [2,70,5,11]

clf.fit(values, sums)
print clf.predict([[0,0],[1,1],[100,0],[1000,2],[100000,10]])