## A function to generate an d-dimensional Gaussian data

import numpy as np
from numpy import random
import matplotlib.pyplot as plt

##Function to generate the gaussian data with the required mean and variance
## Inputs: mean(d-dimensional row vector)\
##	   S(d*d symmetric and positive definite matrix) i.e. the co-variance matrix
##	   N(The number of data points required)	
def gaussian_generator(mean,S,N):
	Sqrt_of_S = np.sqrt(S)
	Sqrt_of_S = np.mat(Sqrt_of_S)
	d = len(mean)
	D = random.randn(N,d)
	D = np.mat(D)
	
	
	for i in range(0,N):
		D[i,:] = mean +  D[i,:]*Sqrt_of_S

	return D
 
a = np.array([4,2])	## The mean matrix
b = np.array([[3,0],[0,3]])	## The covariance matrix
c = 10000		## number of points required

D = gaussian_generator(a,b,c)

fig = plt.figure()
plt.scatter(D[:,0],D[:,1])
plt.show()	
