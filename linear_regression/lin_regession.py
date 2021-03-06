# David Curry
# Gradient Descent using SciKit - Machine Learning

import pylab as pl
import numpy as np
from sklearn import datasets, linear_model

print '---> Importing the Dataset'
data = np.loadtxt('mlclass-ex1-005/mlclass-ex1/ex1data1.txt', delimiter=',')

x = data[:, 0]
y = data[:, 1]

# Create linear regression object
regr = linear_model.LinearRegression()

# Data must be in numpy matrix form: [num samples, num features]
xx = x.reshape((x.shape[0],-1))
yy = y.reshape((y.shape[0],-1))


print '---> Performing Gradient Descent. Training on Dataset'
# Train the model using the training sets
regr.fit(xx, yy)

print ' Coefficent = ', regr.coef_
print ' Intercept  = ', regr.intercept_

theta = [regr.intercept_, regr.coef_]

#Add a column of ones to X (interception data)
it = np.ones(shape=(x.size, 2))

it[:, 1] = x

# the final fit answer is a dot product between theta matrix and x matrix
fit = it.dot(theta)

#predicting some values
print 'If the population is 12,000, the house value(int thousands) = ', regr.predict(12)

print '---> Plotting the Dataset'
pl.scatter(x, y, marker='o', c='b')
pl.plot(x, fit)
pl.title('Profits distribution')
pl.xlabel('Population of City in 10,000s')
pl.ylabel('Profit in $10,000s')
pl.show()



