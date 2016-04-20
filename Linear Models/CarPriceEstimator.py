from sklearn import linear_model
import math

clf = linear_model.Ridge (alpha = .5)

#Top Speed, 0-100 Time
print "Loading features..."
features = [[320, 4], [260, 6.2], [170, 9], [115, 11], [210, 6], [195, 7.5], [225, 6.9], [217, 6.6]]
feature_names = ["Topspeed", "0-100km/h Time"]

#Price in $
print "Loadig prices..."
prices = [675000,  110000, 24000, 19000, 35000, 31000, 42000, 41000]

print "Fitting data to a model..."
clf.fit(features, prices)

#Get input from user
topSpeed = int(raw_input("Top Speed (km/h): "))
acceleration = int(raw_input("0 -> 100km/h time (s): "))

print "Price: $", int(clf.predict([[topSpeed,acceleration]])[0])
